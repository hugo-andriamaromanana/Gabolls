import { ReactNode } from "react";

type BoardBackgroundProps = {
    children: ReactNode 
}

function BoardBackground( {children}: BoardBackgroundProps) {
    return (
        <div className="h-full bg-senary rounded-2xl overflow-y-auto">
            {children}
        </div>
    );
}

export default BoardBackground;
