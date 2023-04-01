
import './App.css';
import UploadFile from './Components/UploadFile';
import { Button} from 'antd';
import DataTable from './Components/Table';
import DatePicker_range from './Components/DatePicker';
function App() {



  return (
    <>
       <div className="container">
        <div className='innerBox'>
        <div className='fileUpload'>
<label>Upload Csv </label>
   <UploadFile/>
        </div>

        <div className='tableSection'>
        <label >Select Date Range</label>
          <div className='daterangeBox'>
           
          <DatePicker_range  />
         
          </div>
          <div className='Table_box'>
          <DataTable/>
          </div>
        </div>
        </div>


    </div>
    </>
 
  );
}

export default App;
