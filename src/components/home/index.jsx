import React, { } from 'react'
import ProjectTimeBar from './project_time_bar'
import EmployeeTimeTable from './employee_time_table'
import CncTime from './cnc_time'
import MonthlyProduction from './monthly_production'
import WeeklyProduction from './weekly_production'
import { ResponsiveContainer } from 'recharts'

const Home = () => {
    return (
        <div>
            <ResponsiveContainer width="100%" height="100%">
                <CncTime />
                <div class='grid grid-col-1 :grid-col-2 gap-8 mb-8'>
                    <ProjectTimeBar />
                    <EmployeeTimeTable />
                </div>
                <div class='grid grid-col-1 :grid-col-2 gap-8 mb-8'>
                    <MonthlyProduction />
                    <WeeklyProduction />
                </div>
            </ResponsiveContainer>
        </div>
    )
}

export default Home 