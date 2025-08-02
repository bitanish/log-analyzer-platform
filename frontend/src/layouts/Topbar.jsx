import {useNavigate} from 'react-router-dom';

export default function Topbar() {
    const handleLogout = () => {
        localStorage.removeItem("token");
        const navigate = useNavigate();
        navigate("/");
    }

    return(
        <header
            style={{
                backgroundColor: '#1f2937',
                color: 'white',
                padding: '10px 20px',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
            }}
        >
            <h2>DevTrack</h2>
            <button onClick={handleLogout} style={{ background: 'none', color: 'white', border: '1px solid white', padding: '5px 10px' }}>
                LogOut
            </button>
        </header>
    );
};