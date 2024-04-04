import { ReactNode } from "react";

type BoardBackgroundProps = {
    children: ReactNode 
}

function BoardBackground( {children}: BoardBackgroundProps) {
    return (
        <div>
            {children}
        </div>
    );
}

export default BoardBackground;
