import LoginForm from '../features/auth/LoginForm';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Grid, Paper, Typography, Box } from '@mui/material';

export default function LoginPage() {
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (token) navigate("/dashboard");
    }, [navigate]);

    return (
        <Box
            sx={{
                minHeight: '100vh',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: '#ebf3fc'
            }}
        >
            <Paper
                elevation={10}
                sx={{
                    p: { xs: 4, sm: 6, md: 8 },
                    borderRadius: 3,
                    maxWidth: 500,
                    width: '100%',
                    textAlign: 'center',
                    backgroundColor: 'rgba(255, 255, 255, 0.95)'
                }}
            >
                <Typography variant="h3" component="h1" gutterBottom sx={{ color: '#333', fontWeight: 600 }}>
                    Welcome
                </Typography>
                <Typography variant="h6" component="p" gutterBottom sx={{ color: '#555', mb: 4 }}>
                    Please login to continue
                </Typography>
                <LoginForm />
            </Paper>
        </Box>
    );
}