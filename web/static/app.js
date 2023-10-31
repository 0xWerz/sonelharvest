const form = document.getElementsByTagName("form")[0]

let country = "", target = "", tags = []
form.addEventListener("submit", () => {
    const input = document.getElementsByTagName("input")
    const export_type = document.getElementsByTagName("select")[0].value
    country = input[0].value === "" ? "DZ" : input[0].value
    target = input[1].value === "" ? "power" : input[1].value
    tags = input[2].value.replaceAll(" ", "").split(",")
    if (tags[0] === '')
        return document.getElementById('res').textContent = "Please enter the tags to query"

    document.getElementById('res').textContent = "Please wait for the response..."
    sendForm(country, target, tags)
})

function sendForm(country, target, tags) {
    fetch("/export", {
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
        const textarea = document.getElementsByTagName("textarea")[0]
        const dwnld = document.getElementById('dwnld')
        if (res.status !== 200) return res.json().then((j) => restext.textContent = j.error)

        res.json().then((j) => {
            textarea.textContent = JSON.stringify(j, null, 3);
            dwnld.removeAttribute("hidden")
            dwnld.addEventListener("click", () => {
                const blob = new Blob([JSON.stringify(j, null, 3)], { type: "application/json" })
                const url = URL.createObjectURL(blob)
                const a = document.createElement("a")
                a.href = url

                console.log("country", country, "target", target)
                a.download = `${country}_${target}_${tags.join("_")}.json`
                a.click()
            })
        })
        console.log(country, target)
    }).catch(e => {
        console.log("err", e)
    })
}