# Week 2: Javascript and the DOM

Following the example of sorting, which we did in class, we'll finish wiring up the functionality of the page.

## Task 1 - Replicate dynamic loading, simple bar chart, Bootstrap buttons, and sort
As we did together in class, and as shown in the code on the master branch of this repository, we need to dynamically populate the table with data from JSON we create with [Mr. Data Converter](https://shancarter.github.io/mr-data-converter/), add a column that uses DIVs sized relative to the cell width to create a bar chart effect, buttons from Bootstrap for our controls, and the ability to sort the data in ascending or descending order. In the commits tab, you can watch these features being added step by step.

The final code has lots of comments, but also consider raising questions in a way that anyone in the class can see by [opening an issue](https://github.com/JHU-DataViz-Summer16/week-2-js-dom/issues/new) in the [issues tab](https://github.com/JHU-DataViz-Summer16/week-2-js-dom/issues).

## Task 2 - Filter
Add a set of buttons that filter the data. If you don't have a categorical variable in your data, you might fake one by, for example, creating filters based on the first letter of a variable, i.e. all the names starting with 'A'. You'll probably need the [Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) method.

```js
var arr = [{ 'name': 'fred', 'age': 30 }, { 'name': 'barney', 'age': 40 }]

var filtered = arr.filter(function (d) { return d.age > 30; })
// [{ 'name': 'barney', 'age': 40 }]
```

## Stretch Task - Pagination
Instead of showing all of the rows on a single page, let's break them up into smaller pages of maybe 15 or 20 rows each. We added a `page` property to the options object in class, setting its initial value to `0`. The next/previous buttons should increment/decrement this value. In order to select the rows of data for the given page, you'll probably need the [Array.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) method.

```js
var arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

var sliced = arr.slice(1, 5)
// ['b', 'c', 'd', 'e']
```

## Troubleshooting

#### "I'm filtering/slicing, but nothing's happening..."

Remember that unlike Array.sort, which sorts the data in place (also known as "mutating" it), Array.filter and Array.slice return new arrays, leaving the original array untouched. So while the sort operation we did in class could just call `data.sort(...)`, the new operations you're creating will need to assign the returned array back to the `data` variable, replacing the original array. So they might look something like this: `data = data.filter(...)`
