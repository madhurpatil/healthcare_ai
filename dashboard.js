async function loadAnalytics() {
    let res = await fetch("/analytics");
    let data = await res.json();

    new Chart(document.getElementById("casesChart"), {
        type: "bar",
        data: {
            labels: ["Total Cases", "Emergency Cases"],
            datasets: [{
                label: "Cases",
                data: [data.total_cases, data.emergency_cases]
            }]
        }
    });

    new Chart(document.getElementById("keywordChart"), {
        type: "pie",
        data: {
            labels: Object.keys(data.keyword_stats),
            datasets: [{
                data: Object.values(data.keyword_stats)
            }]
        }
    });
}

loadAnalytics();