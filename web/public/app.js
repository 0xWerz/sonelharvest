const form = document.getElementsByTagName("form")[0]

let country = "", target = "", tags = []
form.addEventListener("submit", () => {
    const input = document.getElementsByTagName("input")
    const export_type = document.getElementsByTagName("select")[0].value
    country = input[0].value ?? "DZ"
    target = input[1].value ?? "power"
    tags = input[2].value.replaceAll(" ", "").split(",")
    if (tags[0] === '')
        return document.getElementById('res').textContent = "Please enter the tags to query"

    document.getElementById('res').textContent = "Please wait for the response..."
    sendForm(country, target, tags)
})

function sendForm(country, target, tags) {
    fetch("/api/export", {
        method: "POST",
        body: JSON.stringify({
            country,
            target,
            tags
        }),
        headers: {
            "content-type": "application/json"
        }
    }).then((res) => {
        const restext = document.getElementById('res')
        const textarea = document.getElementsByTagName("textarea")[0]
        if (res.status !== 200) return res.json().then((j) => restext.textContent = j.error)

        res.json().then((j) => {
            restext.textContent = "Done."
            textarea.textContent = JSON.stringify(j, null, 3);
        })
    }).catch(e => {
        console.log("err", e)
    })
}