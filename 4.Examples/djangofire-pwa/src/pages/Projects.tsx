import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Card from 'react-bootstrap/Card';
import { createProject, updateProject, deleteProject, getCachedProjects, getProjects, Project, ProjectFields } from '../functions/projects';

interface ProjectCardProps {
  project: Project
  busy: boolean
  onUpdate: (id: number, data: ProjectFields) => Promise<void>
  onDelete: (id: number) => Promise<void>
}

const ProjectCard = (props: ProjectCardProps) => {
  const { busy, onUpdate, onDelete } = props;
  const [editMode, setEditMode] = useState(false);
  const { id, title, color } = props.project;
  const [inputTitle, setInputTitle] = useState(title);

  const handleUpdate = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    await onUpdate(id, {
      title: inputTitle,
      color: color
    })
    setEditMode(false);
  }

  useEffect(() => {
    setInputTitle(title)
  }, [editMode, title]);

  return (
    <Card key={id} border={color} className="mt-2">
      <Card.Body>
        <div className="row">
          <div className="col">
            {editMode ? <Form onSubmit={handleUpdate}>
              <Form.Group className="mb-3" controlId="teamTitleX">
                <Form.Label>Nuevo nombre</Form.Label>
                <Form.Control type="text" placeholder="Nombre del proyecto" value={inputTitle} onChange={(e) => setInputTitle(e.target.value)} disabled={busy} />
              </Form.Group>
              <Button type="submit" variant="success" size="sm" disabled={busy}>
                Actualizar
              </Button>
            </Form> : <Card.Title className="m-0">
              {title}
            </Card.Title>}
          </div>
          {editMode ? <div className="col-auto">
            <Button variant="warning" size="sm" disabled={busy} onClick={() => setEditMode(false)}>
              Cancelar
            </Button>
          </div> : <div className="col-auto">
            <Button variant="primary" size="sm" disabled={busy} onClick={() => setEditMode(true)}>
              Editar
            </Button>
            <Button variant="danger" size="sm" disabled={busy} onClick={() => onDelete(id)}>
              Eliminar
            </Button>
          </div>}
        </div>
      </Card.Body>
    </Card>
  )
}

const ProjectsSection = () => {

  const [projectItems, setProjectItems] = useState(getCachedProjects());
  const [inputTitle, setInputTitle] = useState('');
  const [busy, setBusy] = useState(false);

  const handleNew = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    setBusy(true);
    try {
      if (!inputTitle) {
        throw new Error('Rellene todos los campos');
      }
      await createProject({
        title: inputTitle,
        color: 'primary',
      });
      setInputTitle('');
      getProjects().then(items => setProjectItems(items));
    } catch (err) {
      alert(err.toString());
      console.error(err);
    }
    setBusy(false);
  }

  const handleDelete = async (id: number) => {
    setBusy(true);
    try {
      await deleteProject(id);
      getProjects().then(items => setProjectItems(items));
    } catch (err) {
      alert(err.toString());
      console.error(err);
    }
    setBusy(false);
  }

  const handleUpdate = async (id: number, data: ProjectFields) => {
    setBusy(true);
    try {
      await updateProject(id, data);
      getProjects().then(items => setProjectItems(items));
    } catch (err) {
      alert(err.toString());
      console.error(err);
    }
    setBusy(false);
  }

  useEffect(() => {
    getProjects().then(items => setProjectItems(items));
  }, []);

  return (
    <section id="projects" className="mt-3">
      <h2>Proyectos</h2>
      <Form onSubmit={handleNew}>
        <Form.Group className="mb-3" controlId="teamTitle">
          <Form.Label>Nuevo proyecto</Form.Label>
          <Form.Control type="text" placeholder="Nombre del proyecto" value={inputTitle} onChange={(e) => setInputTitle(e.target.value)} disabled={busy} />
        </Form.Group>
        <Button type="submit" variant="success" size="sm" disabled={busy}>
          Guardar
        </Button>
      </Form>
      {projectItems.map(project => (
        <ProjectCard key={project.id} project={project} busy={busy} onUpdate={handleUpdate} onDelete={handleDelete} />
      ))}
    </section>
  )
}

export default ProjectsSection;
