from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from .database import User, Transaction
from . import schemas
from .auth import get_password_hash, verify_password
from datetime import datetime, timedelta
from typing import Optional, List

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# Transaction CRUD
def create_transaction(db: Session, transaction: schemas.TransactionCreate, user_id: int):
    db_transaction = Transaction(
        **transaction.model_dump(),
        user_id=user_id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(
    db: Session, 
    user_id: int, 
    skip: int = 0, 
    limit: int = 100,
    category: Optional[str] = None,
    transaction_type: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    if category:
        query = query.filter(Transaction.category == category)
    if transaction_type:
        query = query.filter(Transaction.transaction_type == transaction_type)
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    return query.order_by(Transaction.date.desc()).offset(skip).limit(limit).all()

def get_transaction(db: Session, transaction_id: int, user_id: int):
    return db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user_id
    ).first()

def update_transaction(
    db: Session, 
    transaction_id: int, 
    transaction_update: schemas.TransactionUpdate, 
    user_id: int
):
    db_transaction = get_transaction(db, transaction_id, user_id)
    if not db_transaction:
        return None
    
    update_data = transaction_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_transaction, field, value)
    
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int, user_id: int):
    db_transaction = get_transaction(db, transaction_id, user_id)
    if not db_transaction:
        return None
    
    db.delete(db_transaction)
    db.commit()
    return db_transaction

# Dashboard stats
def get_dashboard_stats(db: Session, user_id: int):
    transactions = db.query(Transaction).filter(
        Transaction.user_id == user_id
    ).all()
    
    total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    total_expenses = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    
    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": total_income - total_expenses,
        "transaction_count": len(transactions)
    }

def get_category_breakdown(db: Session, user_id: int, transaction_type: str):
    results = db.query(
        Transaction.category,
        func.sum(Transaction.amount).label('total')
    ).filter(
        Transaction.user_id == user_id,
        Transaction.transaction_type == transaction_type
    ).group_by(Transaction.category).all()
    
    total = sum(r.total for r in results)
    
    return [
        {
            "category": r.category,
            "total": r.total,
            "percentage": round((r.total / total * 100), 2) if total > 0 else 0
        }
        for r in results
    ]

def get_monthly_summary(db: Session, user_id: int, months: int = 6):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=30*months)
    
    transactions = db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.date >= start_date,
        Transaction.date <= end_date
    ).all()
    
    monthly_data = {}
    for t in transactions:
        month_key = t.date.strftime("%Y-%m")
        if month_key not in monthly_data:
            monthly_data[month_key] = {"income": 0, "expenses": 0}
        
        if t.transaction_type == 'income':
            monthly_data[month_key]["income"] += t.amount
        else:
            monthly_data[month_key]["expenses"] += t.amount
    
    return [
        {
            "month": month,
            "income": data["income"],
            "expenses": data["expenses"]
        }
        for month, data in sorted(monthly_data.items())
    ]
