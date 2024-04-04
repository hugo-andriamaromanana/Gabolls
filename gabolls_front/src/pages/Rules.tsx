import { useNavigate } from "react-router-dom";
import CancelButton from "../molecules/CancelButton";
import MediumTitle from "../atoms/Titles/MediumTitle";
import RulesBoard from "../organisms/RulesBoard";

const Rules = () => {
  const navigate = useNavigate();
  return (
    <div className="h-screen bg-quinary">
      <CancelButton type="x" onClick={() => navigate("/count")} />
      <div className="absolute justify-center top-1/4 left-1/2 -translate-y-10">
        <MediumTitle title="Rules" />
      </div>
      <div className='flex flex-col h-full justify-center items-center pt-12'>
                <div className='flex w-8/12 h-4/6 justify-center overflow-y-auto mt-6 pt-12'>
                 <RulesBoard />
        </div>
      </div>
    </div>
  );
};

export default Rules;
