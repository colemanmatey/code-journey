
function NASA({data}) {

    return (
        <div>
            <h3>{ data.title }</h3>
            <img src={ data.url } width="500" alt="" />
            <p>{ data.explanation }</p>
        </div>
    )
}

export default NASA;