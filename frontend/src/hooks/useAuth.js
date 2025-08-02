import { loginUser } from '../services/auth';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export const useAuth = () => {
    const [loading,setLoading] = useState(false);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const login = async (email,password) => {
        setLoading(true);
        setError(null);
        try {
            const res = await loginUser(email,password);
            localStorage.setItem("token",res.token);
            navigate("/dashboard");
        } catch(err) {
            setError(err.message || 'Login Failed');
        } finally {
            setLoading(false);
        }
    }

    return {login, error, loading, setError, setLoading};
};