from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Transaction schemas
class TransactionBase(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None
    transaction_type: str  # 'income' or 'expense'
    date: datetime

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    category: Optional[str] = None
    description: Optional[str] = None
    transaction_type: Optional[str] = None
    date: Optional[datetime] = None

class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Auth schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Dashboard schemas
class DashboardStats(BaseModel):
    total_income: float
    total_expenses: float
    balance: float
    transaction_count: int

class CategoryBreakdown(BaseModel):
    category: str
    total: float
    percentage: float

class MonthlyData(BaseModel):
    month: str
    income: float
    expenses: float
