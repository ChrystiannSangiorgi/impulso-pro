import { useAuth } from '../contexts/AuthContext'

export default function Dashboard() {
  const { usuario, logout } = useAuth()

  return (
    <div className="min-h-screen bg-gray-950 flex items-center justify-center">
      <div className="bg-gray-900 p-8 rounded-2xl text-center max-w-md w-full">
        <h1 className="text-2xl font-bold text-white mb-1">
          Bem-vindo ao <span className="text-orange-500">Impulso Pro</span>
        </h1>
        
        {usuario && (
          <div className="mt-4 mb-6 bg-gray-800 rounded-xl p-4 text-left space-y-2">
            <p className="text-gray-400 text-sm">
              <span className="text-gray-500">Nome:</span>{' '}
              <span className="text-white">{usuario.nome}</span>
            </p>
            <p className="text-gray-400 text-sm">
              <span className="text-gray-500">E-mail:</span>{' '}
              <span className="text-white">{usuario.email}</span>
            </p>
            <p className="text-gray-400 text-sm">
              <span className="text-gray-500">Perfil:</span>{' '}
              <span className="text-orange-400 font-semibold">{usuario.perfil}</span>
            </p>
          </div>
        )}

        <button
          onClick={logout}
          className="w-full bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg py-2 text-sm transition"
        >
          Sair
        </button>
      </div>
    </div>
  )
}