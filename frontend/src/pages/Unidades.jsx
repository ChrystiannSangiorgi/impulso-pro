import { useState, useEffect } from 'react'
import { useAuth } from '../contexts/AuthContext'
import api from '../services/api'

export default function Unidades() {
  const { usuario, logout } = useAuth()
  const [unidades, setUnidades] = useState([])
  const [carregando, setCarregando] = useState(true)
  const [erro, setErro] = useState('')
  const [formulario, setFormulario] = useState(false)
  const [dados, setDados] = useState({
    Nome_Restaurante: '',
    endereco: {
      Cep: '', Estado: '', Cidade: '',
      Bairro: '', Rua: '', Numero_Local: '', Complemento_Local: ''
    }
  })

  async function carregarUnidades() {
    try {
      const response = await api.get('/restaurantes')
      setUnidades(response.data)
    } catch {
      setErro('Erro ao carregar unidades.')
    } finally {
      setCarregando(false)
    }
  }

  useEffect(() => {
    carregarUnidades()
  }, [])

  async function handleCriar() {
    try {
      await api.post('/restaurantes', dados)
      setFormulario(false)
      setDados({
        Nome_Restaurante: '',
        endereco: {
          Cep: '', Estado: '', Cidade: '',
          Bairro: '', Rua: '', Numero_Local: '', Complemento_Local: ''
        }
      })
      carregarUnidades()
    } catch {
      setErro('Erro ao criar unidade.')
    }
  }

  async function handleAlternarStatus(id) {
    try {
      await api.patch(`/restaurantes/${id}/status`)
      carregarUnidades()
    } catch {
      setErro('Erro ao alterar status.')
    }
  }

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
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold">Unidades da Rede</h2>
          <button
            onClick={() => setFormulario(!formulario)}
            className="bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg px-4 py-2 text-sm transition"
          >
            {formulario ? 'Cancelar' : '+ Nova Unidade'}
          </button>
        </div>

        {erro && <p className="text-red-400 text-sm mb-4">{erro}</p>}

        {/* Formulário */}
        {formulario && (
          <div className="bg-gray-900 rounded-2xl p-6 mb-6 space-y-4">
            <h3 className="font-semibold text-lg">Nova Unidade</h3>
            <input
              placeholder="Nome do restaurante"
              value={dados.Nome_Restaurante}
              onChange={(e) => setDados({ ...dados, Nome_Restaurante: e.target.value })}
              className="w-full bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500"
            />
            <div className="grid grid-cols-2 gap-3">
              <input placeholder="CEP" value={dados.endereco.Cep}
                onChange={(e) => setDados({ ...dados, endereco: { ...dados.endereco, Cep: e.target.value } })}
                className="bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500" />
              <input placeholder="Estado (UF)" value={dados.endereco.Estado}
                onChange={(e) => setDados({ ...dados, endereco: { ...dados.endereco, Estado: e.target.value } })}
                className="bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500" />
              <input placeholder="Cidade" value={dados.endereco.Cidade}
                onChange={(e) => setDados({ ...dados, endereco: { ...dados.endereco, Cidade: e.target.value } })}
                className="bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500" />
              <input placeholder="Bairro" value={dados.endereco.Bairro}
                onChange={(e) => setDados({ ...dados, endereco: { ...dados.endereco, Bairro: e.target.value } })}
                className="bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500" />
              <input placeholder="Rua" value={dados.endereco.Rua}
                onChange={(e) => setDados({ ...dados, endereco: { ...dados.endereco, Rua: e.target.value } })}
                className="bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500" />
              <input placeholder="Número" value={dados.endereco.Numero_Local}
                onChange={(e) => setDados({ ...dados, endereco: { ...dados.endereco, Numero_Local: e.target.value } })}
                className="bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500" />
              <input placeholder="Complemento (opcional)" value={dados.endereco.Complemento_Local}
                onChange={(e) => setDados({ ...dados, endereco: { ...dados.endereco, Complemento_Local: e.target.value } })}
                className="bg-gray-800 rounded-lg px-4 py-2 text-sm outline-none focus:ring-2 focus:ring-orange-500 col-span-2" />
            </div>
            <button
              onClick={handleCriar}
              className="w-full bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg py-2 text-sm transition"
            >
              Criar Unidade
            </button>
          </div>
        )}

        {/* Lista de unidades */}
        {carregando ? (
          <p className="text-gray-400 text-sm">Carregando...</p>
        ) : unidades.length === 0 ? (
          <p className="text-gray-400 text-sm">Nenhuma unidade cadastrada.</p>
        ) : (
          <div className="space-y-4">
            {unidades.map((u) => (
              <div key={u.ID_Restaurante} className="bg-gray-900 rounded-2xl p-5 flex justify-between items-start">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <h3 className="font-semibold">{u.Nome_Restaurante}</h3>
                    <span className={`text-xs px-2 py-0.5 rounded-full ${u.Atividade ? 'bg-green-900 text-green-400' : 'bg-red-900 text-red-400'}`}>
                      {u.Atividade ? 'Ativa' : 'Inativa'}
                    </span>
                  </div>
                  <p className="text-gray-400 text-sm">
                    {u.endereco.Rua}, {u.endereco.Numero_Local} — {u.endereco.Bairro}, {u.endereco.Cidade}/{u.endereco.Estado}
                  </p>
                </div>
                <button
                  onClick={() => handleAlternarStatus(u.ID_Restaurante)}
                  className="text-xs text-gray-500 hover:text-white border border-gray-700 hover:border-gray-500 rounded-lg px-3 py-1 transition"
                >
                  {u.Atividade ? 'Inativar' : 'Ativar'}
                </button>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}