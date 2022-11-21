import { Page } from "./mutations";

export interface Todo {
  id: string;
  text: string;
  checked: boolean;
}

export interface State {
  username: string;
  showHeader: boolean;
  page: string;
  todos: Array<Todo>;
  errors: string;
  credentials: {
    username: string;
    password: string;
  };
}

export const createInitialState = (): State => ({
  username: null,
  showHeader: true,
  page: Page.Home,
  todos: [],
  errors: null,
  credentials: null,
});
