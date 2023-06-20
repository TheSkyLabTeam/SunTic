'use client'

import { useEffect, useState } from "react"
import './styleComponents/PanelDeControl.css'
import { StaticDatePicker } from "@mui/x-date-pickers/StaticDatePicker";
import dayjs from "dayjs";

export default function PanelDeControl() {

    const [panel, setPanel] = useState(false);
    const [state, setState] = useState('un-active');
    const [date, setDate] = useState(dayjs());
    const [day, setDay] = useState();
    const [month, setMonth] = useState();
    const [year, setYear] = useState();

    console.log(date);

    /* Extracting data from date*/ 

    useEffect(() => {
        /* Extracting the day from date */
        setDay(date['$D']);
        /* Extracting the month from date */
        setMonth(date['$M'] + 1);
        /* Extracting the year from date */
        setYear(date['$y']);

    }, [date])

    useEffect(() => {
      
        if (panel == false) {
            setState('un-active');
        } if(panel == true) {
            setState('active');
        }

    }, [panel]);

    // Changin the State of the control panel

    const changeState = () => {
        if (panel == false) {
            setPanel(true)
        }
        if(panel == true) {
            setPanel(false)
        }
    }
    

    return (
        <div className={`panelDeControl ${state} flex flex-col gap-2 w-full p-4 sticky top-[92vh] rounded-xl bg-primary transition-all duration-300`}>
            <div className="flex text-on-primary font-semibold justify-between" id="simplePanelContainer">
                <div className={`panelTitleContainer ${state}`}>
                    <h1 id="panelTitle" className=" w-60">Panel de control</h1>
                    {/* Elements that will be displayed when the state is un-active*/}
                    <div id="resumePanelElements" className={`flex flex-col w-full ${state}`}>
                        <div id="resumeDisplayImage" className=" w-48 h-8 border rounded-lg"></div>
                    </div>
                </div>
                <button className="w-8 h-8 bg-primary-container rounded-full" onClick={changeState}></button>
            </div>
            <div id="panelToolsContainer" className={`flex flex-row gap-4 ${state}`}>
                <div id="ImageDisplay" className=" h-96 w-96 border-on-primary border-2 rounded-3xl"></div>
                <StaticDatePicker defaultValue={date} onChange={setDate} orientation="landscape"/>
            </div>
        </div>
    )

}