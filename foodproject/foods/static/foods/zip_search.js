"use strict";
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
class Zipcode extends React.Component { }





const domContainer = document.querySelector("#zip_search");
ReactDOM.render(<Zipcode />, domContainer);

//create constructor, super props, state
//grab input from form 
//send get request via axios. grab address field from own database http://127.0.0.1:8000/address/?value=
//will send a response, we want to render the response on the page.