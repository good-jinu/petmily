import { useState, useEffect } from 'react';
import Calendar from 'react-calendar';
import { post_reservation, get_buisnesshour } from 'jslib/reservation_api';
import 'assets/CSS/Calendar.css';

function Reservation(props) {
    const [selectedDate, setSelectedDate] = useState(new Date());
    let hname = null;
    let timeSelectionBtns = [];
    hname = props.name;

    useEffect(() => {
        get_buisnesshour(props.HospitalID);
    }, [])

    for(let i=18; i<36; i++)
    {
        const hour = parseInt(i/2);
        const minute = (i % 2) * 30;
        selectedDate.setHours(hour);
        selectedDate.setMinutes(minute);
        const tstmp = selectedDate.getTime();
        const clickbtn = (e) => {
            let data = {
                HospitalID: props.HospitalID,
                Customer_name:'이진우',
                Customer_number:'010-1234-1234',
                AnimalType: '개',
                Symptom: '결막염',
                Time: tstmp
            };
            post_reservation(data);
        }
        timeSelectionBtns.push(<button onClick={clickbtn}>{`${hour}:${minute}`}</button>);
    }
    
    return (
        <div>
            <h1>{hname}</h1>
            <div className="calendar-container">
                <Calendar onChange={setSelectedDate} value={selectedDate}/>
            </div>
            <div className="time-selection-container">
                <h1>
                    {`${selectedDate.getFullYear()}년 ${selectedDate.getMonth() + 1}월 ${selectedDate.getDate()}일`}
                </h1>
                <div className="time-selection">
                    {timeSelectionBtns}
                </div>
            </div>
        </div>
    );
}

export default Reservation;