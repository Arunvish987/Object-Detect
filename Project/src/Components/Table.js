import React from 'react'
import { Space, Table, Tag } from 'antd';

const DataTable = () => {
    const dataSource = [
        {
          key: '1',
          name: 'Mike',
          age: 32,
          address: '10 Downing Street',
        },
        {
          key: '2',
          name: 'John',
          age: 42,
          address: '10 Downing Street',
        },
      ];
      
      const columns = [
        {
          title: 'Image Name',
          dataIndex: 'name',
          key: 'name',
        },
        {
          title: 'Detections',
          dataIndex: 'age',
          key: 'age',
        },
        {
          title: 'Image',
          dataIndex: 'address',
          key: 'address',
        },
      ]
  return (
    <>
    <Table dataSource={dataSource} columns={columns} />
    </>
  )
}

export default DataTable