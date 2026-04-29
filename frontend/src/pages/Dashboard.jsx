import { useAuth } from '../contexts/AuthContext'
import { useNavigate } from 'react-router-dom'

export default function Dashboard() {
  const { usuario, logout } = useAuth()
  const navigate = useNavigate()

  return (
    <div className="min-h-screen bg-gray-950 text-white">
      {/* Header */}
      <header className="bg-gray-900 px-8 py-4 flex justify-between items-center border-b border-gray-800">
        <h1 className="text-xl font-bold">
          Impulso <span className="text-orange-500">Pro</span>
        </h1>
        <div className="flex items-center gap-4">
          <span className="text-sm text-gray-400">
            {usuario?.nome} — <span className="text-orange-400">{usuario?.perfil}</span>
          </span>
          <button onClick={logout} className="text-sm text-gray-500 hover:text-white transition">
            Sair
          </button>
        </div>
      </header>

      {/* Conteúdo */}
      <main className="max-w-4xl mx-auto px-8 py-8">
        <h2 className="text-2xl font-bold mb-6">Bem-vindo, {usuario?.nome}!</h2>

        <div className="grid grid-cols-2 gap-4">
          <button
            onClick={() => navigate('/unidades')}
            className="bg-gray-900 hover:bg-gray-800 border border-gray-800 hover:border-orange-500 rounded-2xl p-6 text-left transition"
          >
            <p className="text-orange-500 text-2xl mb-2">🏪</p>
            <h3 className="font-semibold text-lg">Unidades</h3>
            <p className="text-gray-400 text-sm mt-1">Gerenciar unidades da rede</p>
          </button>
        </div>
      </main>
    </div>
  )
}