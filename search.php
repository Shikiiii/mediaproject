<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Results</title>
    <style>
    table, th, td {
        border:1px solid black;
    }
    </style>
</head>
<body>
    <fieldset>
    <legend>Controls</legend>
        <a href="http://127.0.0.1:8000/addnewitem">
            <input type="button" value="Add new item"/>
        </a>
        <a href="http://127.0.0.1:8000/removeitem">
            <input type="button" value="Remove an item"/>
        </a>
        <a href="http://127.0.0.1:8000/rentitem">
            <input type="button" value="Mark item as rented"/>
        </a>
        <a href="http://127.0.0.1:8000/unrentitem">
            <input type="button" value="Unmark item as rented"/>
        </a>
    </fieldset>
    <br><hr>
    <h2>Search results:</h2>
    <form>
        <input type="checkbox" id="item1"/>
        <label for="name1">000001, Twilight, Volume 3, 5/10/2022, Yes, 3/10/2022, 10/10/2022, AGAWJK295820NGENKG</label>
        <br><br><br>
        <input type="submit" id="action" value="Delete selected items"/>
        <input type="submit" id="action" value="Mark selected items as rented"/>
        <input type="submit" id="action" value="Unmark selected items as rented"/>
        <a href="http://127.0.0.1:8000/">
            <input type="button" value="Go back">
        </a>
    </form>
</body>
</html>
