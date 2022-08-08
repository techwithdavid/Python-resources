import React from 'react';
import Button from 'react-bootstrap/Button';

import { loginWithGoogle } from '../functions/auth';

const LoginPage = () => (
  <main className="mt-3">
    <Button onClick={loginWithGoogle}>
      Iniciar sesión con Google
    </Button>
  </main>
)

export default LoginPage;
