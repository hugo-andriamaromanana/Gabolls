

type MiniCardProps = {
    icon: 'A' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' |  'V' | 'D' | 'R';
    icon2?: string;
    pts?: string;
    color? : 'red' | 'black';
    text?: string;
};

const MiniCard = ({ icon, icon2, pts, color, text}: MiniCardProps) => {
    return (
        <div className="flex flex-col justify-start items-center">
        <div className="flex">
        <div className={`border-2 rounded-lg  p-3 m-4 w-10 text-lg ${color==='red' ? "border-red-500 text-red-500" : "border-black text-black"}`}>
            {icon} 
        </div>
        {icon2 && (
        <div className={`border-2 rounded-lg  p-3 m-4 w-10 text-lg ${color==='red' ? "border-red-500 text-red-500" : "border-black text-black"}`}>
            {icon2} 
        </div>
        
    )}
    </div>
        <div className="m-2">
            {pts && (
            <div>
                {pts} pts
            </div>
        )}
        {text && (
            <div>
                {text}
            </div>
        )}
        </div>
        </div>
    );
};

export default MiniCard;
