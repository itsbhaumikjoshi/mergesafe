import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { ThemeProvider, CssBaseline } from "@mui/material"
import { AuthProvider } from "./context/AuthContext"
import { LandingPage } from "./components/home"
import theme from "./styles/home/theme"

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Router>
          <Routes>
            <Route path="/" element={<LandingPage />} />
          </Routes>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  )
}

export default App
