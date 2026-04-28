import { createContext, useContext, useState, useEffect } from 'react'

const AuthContext = createContext(null)

function parseJWT(token) {
  try {
    const base64 = token.split('.')[1]
    const decoded = JSON.parse(atob(base64))
    return decoded
  } catch {
    return null
  }
}

export function AuthProvider({ children }) {
  const [usuario, setUsuario] = useState(null)

  useEffect(() => {
    const token = sessionStorage.getItem('token')
    if (token) {
      const dados = parseJWT(token)
      if (dados) {
        setUsuario({
          id: dados.sub,
          email: dados.email,
          perfil: dados.perfil,
          nome: dados.nome
        })
      }
    }
  }, [])

  function logout() {
    sessionStorage.removeItem('token')
    setUsuario(null)
    window.location.href = '/login'
  }

  return (
    <AuthContext.Provider value={{ usuario, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  return useContext(AuthContext)
}