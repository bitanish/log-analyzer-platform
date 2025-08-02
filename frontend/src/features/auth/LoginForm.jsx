import { useState, useEffect } from 'react';
import { useAuth } from '../../hooks/useAuth';
import Spinner from '../../components/Spinner';
import ErrorFallback from '../../components/ErrorFallback';
import CustomButton from '../../components/CustomButton'; // Assuming this is a custom button component
import {
    Box,
    TextField,
    Typography,
    Button,
    Paper,
} from '@mui/material';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { login, error, loading, setError, setLoading} = useAuth();
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        await login(email, password);
    };

    const handleEmailChange = (e) => {
        if (error) {
            setError(false);
        }
        setEmail(e.target.value);
    }

    const handlePasswordChange = (e) => {
        if (error) {
            setError(false);
        }
        setPassword(e.target.value);
    }

    return (
        <Box>
            <Box
                component="form"
                onSubmit={handleSubmit}
                noValidate
                sx={{ display: 'flex', flexDirection: 'column', gap: 3 }}
            >
                <TextField
                    label="Email"
                    type="email"
                    variant="outlined"
                    fullWidth
                    value={email}
                    onChange={handleEmailChange}
                    required
                    sx={{ '& .MuiOutlinedInput-root': { borderRadius: 2 } }}
                />
                <TextField
                    label="Password"
                    type="password"
                    variant="outlined"
                    fullWidth
                    value={password}
                    onChange={handlePasswordChange}
                    required
                    sx={{ '& .MuiOutlinedInput-root': { borderRadius: 2 } }}
                />

                {error && <ErrorFallback message={error} />}

                {loading ? (
                    <Spinner />
                ) : (
                    <Button
                        type="submit"
                        variant="contained"
                        fullWidth
                        sx={{
                            mt: 2,
                            py: 1.5,
                            borderRadius: 2,
                            fontWeight: 'bold',
                            fontSize: '1rem',
                            letterSpacing: 1,
                            transition: 'transform 0.2s',
                            '&:hover': {
                                transform: 'scale(1.02)'
                            }
                        }}
                    >
                        LOGIN
                    </Button>
                )}
            </Box>
        </Box>
    );
};

export default LoginForm;