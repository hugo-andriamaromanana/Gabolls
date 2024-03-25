import './App.css';

import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import routes from './routes';

import { QueryClient, QueryClientProvider } from 'react-query';

const router = createBrowserRouter(routes);

const queryClient = new QueryClient();

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <RouterProvider router={router} />
        </QueryClientProvider>
    );
}

export default App;
