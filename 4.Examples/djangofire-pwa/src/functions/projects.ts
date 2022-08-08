import { apiURL } from "./api";
import { getHeaders } from "./auth";

export interface ProjectFields {
  title: string;
  color: string;
}

export interface Project extends ProjectFields {
  id: number;
}

export const getCachedProjects = (): Project[] => {
  const data = localStorage.getItem('ALL_PROJECTS');
  if (!data) {
    return [];
  }
  try {
    const items: Project[] = JSON.parse(data);
    return items;
  } catch (error) {
    console.error(error);
    localStorage.removeItem('ALL_PROJECTS');
    return [];
  }
}

export const getProjects = async (): Promise<Project[]> => {
  const headers = await getHeaders();
  const url = `${apiURL}projects`;
  const res = await fetch(url, {
    method: 'GET',
    headers: headers,
    redirect: 'follow'
  });
  if (res.status !== 200) {
    console.error(res);
    throw new Error('Error al cargar Proyectos');
  }
  const body: Project[] = await res.json();
  localStorage.setItem('ALL_PROJECTS', JSON.stringify(body));
  return body;
}

export const createProject = async (item: ProjectFields): Promise<Project> => {
  const headers = await getHeaders();
  const url = `${apiURL}projects/`;
  const res = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(item),
    redirect: 'follow'
  });
  if (res.status !== 201) {
    console.error(res);
    throw new Error('Error al crear Proyecto');
  }
  const body: Project = await res.json();
  return body;
}

export const updateProject = async (id: number, item: ProjectFields): Promise<Project> => {
  const headers = await getHeaders();
  const url = `${apiURL}projects/${id}`;
  const res = await fetch(url, {
    method: 'PATCH',
    headers: headers,
    body: JSON.stringify(item),
    redirect: 'follow'
  });
  if (res.status !== 200) {
    console.error(res);
    throw new Error('Error al actualizar Proyecto');
  }
  const body: Project = await res.json();
  return body;
}

export const deleteProject = async (id: number): Promise<void> => {
  const headers = await getHeaders();
  const url = `${apiURL}projects/${id}`;
  const res = await fetch(url, {
    method: 'DELETE',
    headers: headers,
    redirect: 'follow'
  });
  if (res.status !== 204) {
    console.error(res);
    throw new Error('Error al eliminar Proyecto');
  }
  return;
}
