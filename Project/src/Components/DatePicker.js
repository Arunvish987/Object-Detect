import React,{useState} from 'react'
import { DatePicker,Button } from 'antd';
import { FetchData_And_Generate_report } from '../API';
import axios from 'axios';
const { RangePicker } = DatePicker;
const DatePicker_range = ({ClickHandler}) => {
const[dateRange,setDateRange]=useState([])
     const onChange = (value, dateString) => {
      const formData = new FormData();
      formData.append('from_date', dateString[0])
      formData.append('to_date', dateString[1])
fetch(FetchData_And_Generate_report, {
      method: 'POST',
      body: formData,
    })
      .then((res) => res.json())
      .then(() => {
      })
      .catch(() => {
        
      })
      .finally(() => {
      });
        
      };

      
  return (
   
   <>
   <RangePicker
    onChange={onChange}
    format="YYYY-MM-DD"
   />
    <Button type='primary' style={{marginLeft:"20px"}}>Fetch Data And Generate Report</Button>
   </>
  )
}

export default DatePicker_range