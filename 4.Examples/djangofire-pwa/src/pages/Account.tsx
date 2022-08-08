import React from 'react';
import Button from 'react-bootstrap/Button';
import { useUser } from 'reactfire';
import { logout } from '../functions/auth';

const AccountSection = () => {
  const { data: user } = useUser();
  return (
    <section id="account" className="mt-3">
      <h2>Cuenta</h2>
      <p>{user.displayName} ({user.email})</p>
      <Button onClick={logout} size="sm" variant="danger">
        Cerrar sesión
      </Button>
    </section>
  )
}

export default AccountSection;
