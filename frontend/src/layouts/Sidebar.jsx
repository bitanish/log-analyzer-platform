import { Link } from 'react-router-dom';

export default function Sidebar() {
  return (
    <aside
      style={{
        width: '200px',
        backgroundColor: '#f3f4f6',
        height: '100vh',
        padding: '20px',
        boxSizing: 'border-box'
      }}
    >
      <nav>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li><Link to="/dashboard">Dashboard</Link></li>
          <li><Link to="/logs">Logs</Link></li>
          <li><Link to="/settings">Settings</Link></li>
        </ul>
      </nav>
    </aside>
  );
}
