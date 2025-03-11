function generateColors(count) {
    let colors = [];
    for (let i = 0; i < count; i++) {
        let hue = (i * 360 / count) % 360; // Spread hues evenly around the color wheel
        let saturation = 70; // Keep saturation constant for vivid colors
        let lightness = 50; // Adjust lightness if needed (e.g., 40-60 for contrast)
        colors.push(`hsl(${hue}, ${saturation}%, ${lightness}%)`);
    }
    return colors;
}

// document.addEventListener("DOMContentLoaded", function () {
const ctx = document.getElementById('womensPieChart');
const cty = document.getElementById('mensPieChart');

var female_countries = JSON.parse(document.getElementById('female_countries_counter').textContent);
var male_countries = JSON.parse(document.getElementById('male_countries_counter').textContent);
var all_countries = JSON.parse(document.getElementById('list_countries').textContent);

let countryColors = generateColors(all_countries.length);
let countryColorMap = {};
all_countries.forEach((country, index) => {
    countryColorMap[country] = countryColors[index]; // Assign each country a fixed color
});

let female_backgroundColors = Object.keys(female_countries).map(country => countryColorMap[country]);
let male_backgroundColors = Object.keys(male_countries).map(country => countryColorMap[country]);

new Chart(ctx, {
type: 'pie',
data: {
    labels: Object.keys(female_countries),
    datasets: [{
        label: '# of players',
        data: Object.values(female_countries),
        backgroundColor: female_backgroundColors,
        borderWidth: 1
    }]
},
options: {
    plugins: {
        title: {
            display: true,
            text: "Number of women's singles players per country"
        }
    }
}
});



new Chart(cty, {
type: 'pie',
data: {
    labels: Object.keys(male_countries),
    datasets: [{
        label: '# of players',
        data: Object.values(male_countries),
        backgroundColor: male_backgroundColors,
        borderWidth: 1
    }]
},
options: {
    plugins: {
        title: {
            display: true,
            text: "Number of men's singles players per country"
        }
    }
}
});
// })
