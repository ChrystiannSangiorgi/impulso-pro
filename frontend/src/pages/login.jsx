import { useState } from 'react'
import api from '../services/api'

export default function Login() {
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const [erro, setErro] = useState('')
  const [carregando, setCarregando] = useState(false)

  async function handleLogin() {
    setErro('')
    setCarregando(true)
    try {
      const response = await api.post('/auth/login', { email, senha })
      sessionStorage.setItem('token', response.data.access_token)
      window.location.href = '/dashboard'
    } catch (error) {
      if (error.response?.status === 403) {
        setErro('Conta bloqueada. Entre em contato com o administrador.')
      } else {
        setErro('E-mail ou senha inválidos.')
      }
    } finally {
      setCarregando(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-950 flex items-center justify-center">
      <div className="bg-gray-900 p-8 rounded-2xl shadow-xl w-full max-w-md">
        
        {/* Logo / Título */}
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-white">Impulso <span className="text-orange-500">Pro</span></h1>
          <p className="text-gray-400 mt-2 text-sm">Gestão de treinamentos operacionais</p>
        </div>

        {/* Formulário */}
        <div className="space-y-4">
          <div>
            <label className="text-sm text-gray-400 mb-1 block">E-mail</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="seu@email.com"
              className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 text-sm outline-none focus:ring-2 focus:ring-orange-500 transition"
            />
          </div>

          <div>
            <label className="text-sm text-gray-400 mb-1 block">Senha</label>
            <input
              type="password"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              placeholder="••••••••"
              onKeyDown={(e) => e.key === 'Enter' && handleLogin()}
              className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 text-sm outline-none focus:ring-2 focus:ring-orange-500 transition"
            />
          </div>

          {/* Mensagem de erro */}
          {erro && (
            <p className="text-red-400 text-sm text-center">{erro}</p>
          )}

          {/* Botão */}
          <button
            onClick={handleLogin}
            disabled={carregando}
            className="w-full bg-orange-500 hover:bg-orange-600 disabled:bg-orange-800 text-white font-semibold rounded-lg py-3 text-sm transition"
          >
            {carregando ? 'Entrando...' : 'Entrar'}
          </button>
        </div>
      </div>
    </div>
  )
}