// This keyword

const employee = {
    name: "Max",
    position: "Superintendent",
    wage: 30000,
    supervise() {
        console.log(this);
        console.log(this.wage);
        console.log(wage); // wage is not known
    }
}

employee.supervise(); // function is called because this is bound to the object


const coleman = employee.supervise;
coleman(); // this is no longer bound to the employee object because the function is passed as a reference


const layla = employee.supervise.bind(employee);
layla(); // the supervise method is bound to a specific object