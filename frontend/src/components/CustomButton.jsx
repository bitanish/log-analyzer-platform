export default function CustomButton({ text, onClick, type="submit", disabled=false}){
	return (
		<button
			type={type}
			onClick={onClick}
			disabled={disabled}
			style={{
				padding: '10px 20px',
				backgroundColor: '#007bff',
				color: 'white',
				border: 'none',
				borderRadius: '5px',
				cursor: disabled ? 'not-allowed' : 'pointer',
			}}
		>
      		{text}
    	</button>
	);
};