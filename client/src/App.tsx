import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { ThemeProvider, CssBaseline } from "@mui/material"
import { AuthProvider } from "./context/AuthContext"
import { LandingPage } from "./components/home"
import { ProtectedRoute } from "./components/ProtectedRoute"
import { AppPage } from "./components/app"
import theme from "./styles/home/theme"

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Router>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/app" element={<ProtectedRoute><AppPage /></ProtectedRoute>} />
          </Routes>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  )
}

export default App
