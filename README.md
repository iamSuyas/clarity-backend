# Clarity - Personal Expense Tracking App

Clarity is a modern, full-stack personal expense tracking application that helps you understand your finances better. Built with React, TypeScript, Python FastAPI, and SQLite.

![Clarity Screenshot](screenshot.png)

## Features

### Core Features
- **User Authentication**: Secure signup/login with JWT tokens
- **Transaction Management**: Add, edit, delete income and expenses
- **Multi-Step Form**: Beautiful 3-step wizard for adding transactions
- **Dashboard**: Visual overview with charts and statistics
- **Transaction History**: Filter by category, type, and date range
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works seamlessly on mobile and desktop

### Dashboard
- Total balance, income, and expenses overview
- Monthly income vs expenses bar chart
- Expense breakdown pie chart by category
- Recent transactions list

### Transactions
- Complete CRUD operations
- Advanced filtering by category, type, and date range
- Clean table view with edit/delete actions
- Visual indicators for income (green) vs expenses (red)

## Tech Stack

### Backend
- **Python 3.8+**
- **FastAPI**: Modern, fast web framework
- **SQLAlchemy**: ORM for database operations
- **SQLite**: Lightweight database (easily switchable to PostgreSQL)
- **JWT**: Secure authentication
- **Pydantic**: Data validation

### Frontend
- **React 18** with TypeScript
- **Vite**: Next-gen build tool
- **Tailwind CSS**: Utility-first styling
- **React Router**: Client-side routing
- **Recharts**: Data visualization
- **Axios**: HTTP client
- **Lucide React**: Icon library
- **date-fns**: Date formatting

## Project Structure

```
expense-tracker/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI application
│   │   ├── database.py      # Database models and connection
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── auth.py          # Authentication utilities
│   │   └── crud.py          # CRUD operations
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── context/         # React contexts (Auth, Theme)
│   │   ├── types/           # TypeScript types
│   │   ├── api.ts           # API client
│   │   ├── App.tsx          # Main App component
│   │   └── main.tsx         # Entry point
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── index.html
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create environment file:
```bash
cp .env.example .env
```

6. Run the server:
```bash
python -m app.main
```

The backend will start at `http://localhost:8000`

API documentation will be available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will start at `http://localhost:5173`

## Usage

1. Open your browser and go to `http://localhost:5173`
2. Create a new account or sign in
3. Start tracking your finances!

### Adding a Transaction

1. Click "Add Transaction" button
2. **Step 1**: Select transaction type (Income/Expense) and enter amount
3. **Step 2**: Choose a category from predefined options or enter custom
4. **Step 3**: Add description (optional) and date
5. Review and submit!

### Filtering Transactions

Use the filter bar to:
- Filter by specific categories
- Show only income or expenses
- Filter by date range
- Clear filters anytime

## Environment Variables

### Backend (.env)
```
SECRET_KEY=your-secret-key-here-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./clarity.db
```

## API Endpoints

### Authentication
- `POST /auth/signup` - Create new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user

### Transactions
- `GET /transactions` - List all transactions
- `POST /transactions` - Create transaction
- `GET /transactions/{id}` - Get specific transaction
- `PUT /transactions/{id}` - Update transaction
- `DELETE /transactions/{id}` - Delete transaction

### Dashboard
- `GET /dashboard/stats` - Get dashboard statistics
- `GET /dashboard/categories/{type}` - Get category breakdown
- `GET /dashboard/monthly` - Get monthly summary

## What I'm Most Proud Of

1. **Multi-Step Form**: The transaction creation process is broken down into a beautiful 3-step wizard with progress indicators, making it user-friendly and intuitive.

2. **Dark Mode Implementation**: The entire app supports both light and dark themes with smooth transitions and proper contrast ratios.

3. **Responsive Design**: The application works seamlessly across all device sizes, from mobile phones to large desktop screens.

4. **Clean Architecture**: The codebase follows best practices with clear separation of concerns, reusable components, and type safety throughout.

5. **Real-time Updates**: All CRUD operations reflect immediately in the UI with proper state management.

## What I'd Add With More Time

1. **Data Export**: Export transactions to CSV/Excel
2. **Recurring Transactions**: Set up automatic recurring transactions
3. **Budget Goals**: Set monthly spending limits by category
4. **Receipt Upload**: Attach receipt images to transactions
5. **Data Visualization**: More charts and spending insights
6. **Multi-currency Support**: Track expenses in different currencies
7. **Cloud Database**: Migrate from SQLite to PostgreSQL
8. **Email Notifications**: Weekly/monthly spending reports
9. **API Rate Limiting**: Better security measures
10. **Unit & Integration Tests**: Comprehensive test coverage

## Deployment

### Backend (Railway/Render)
1. Create account on Railway or Render
2. Connect your GitHub repository
3. Set environment variables
4. Deploy!

### Frontend (Vercel/Netlify)
1. Create account on Vercel or Netlify
2. Connect your GitHub repository
3. Build command: `npm run build`
4. Output directory: `dist`
5. Deploy!

## Test Account

For testing purposes, you can create any account:
- Email: test@example.com
- Password: any password (minimum 6 characters)

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue on GitHub.

---

Built with passion for the Software Engineer Intern position at Build Clarity.
