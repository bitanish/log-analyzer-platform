export default function ErrorFallback({ message = "Something went wrong" }) {
  return (
    <div style={{ color: 'red', marginTop: '10px' }}>
      ❌ Invalid credentials
    </div>
  );
}
