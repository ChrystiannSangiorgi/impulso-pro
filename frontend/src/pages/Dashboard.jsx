export default function Dashboard() {
  const token = sessionStorage.getItem('token')

  function handleLogout() {
    sessionStorage.removeItem('token')
    window.location.href = '/login'
  }

  return (
    <div className="min-h-screen bg-gray-950 flex items-center justify-center">
      <div className="bg-gray-900 p-8 rounded-2xl text-center">
        <h1 className="text-2xl font-bold text-white mb-2">
          Bem-vindo ao <span className="text-orange-500">Impulso Pro</span>
        </h1>
        <p className="text-gray-400 text-sm mb-6">Login realizado com sucesso!</p>
        <button
          onClick={handleLogout}
          className="bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg px-6 py-2 text-sm transition"
        >
          Sair
        </button>
      </div>
    </div>
  )
}