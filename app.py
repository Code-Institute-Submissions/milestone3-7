import os
import env

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('DATABASE')
if os.path.exists("env.py"):
    app.config["MONGO_URI"] = env.mongo_uri
else:
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe_list.html", 
                            recipe_data=mongo.db.recipe_data.find())



@app.route('/get_recipe/<recipe_id>')
def about_recipe_details(recipe_id):
    the_recipe = mongo.db.recipe_data.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe_details.html', recipe=the_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipe_data.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe_data = mongo.db.recipe_data
    recipe_data.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'authors_name':request.form.get('authors_name'),
        'recipe_image': request.form.get('recipe_image'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time':request.form.get('cooking_time'),
        'difficulty_rating':request.form.get('difficulty_rating'),
        'ingredients_1':request.form.get('ingredients_1'),
        'ingredients_2':request.form.get('ingredients_2'),
        'ingredients_3':request.form.get('ingredients_3'),
        'ingredients_4':request.form.get('ingredients_4'),
        'ingredients_5':request.form.get('ingredients_5'),
        'ingredients_6':request.form.get('ingredients_6'),
        'ingredients_7':request.form.get('ingredients_7'),
        'ingredients_8':request.form.get('ingredients_8'),
        'ingredients_9':request.form.get('ingredients_9'),
        'ingredients_10':request.form.get('ingredients_10'),
        'ingredients_11':request.form.get('ingredients_11'),
        'ingredients_12':request.form.get('ingredients_12'),
        'ingredients_13':request.form.get('ingredients_13'),
        'ingredients_14':request.form.get('ingredients_14'),
        'ingredients_15':request.form.get('ingredients_15'),
        'ingredients_16':request.form.get('ingredients_16'),
        'method_step_1':request.form.get('method_step_1'),
        'method_step_2':request.form.get('method_step_2'),
        'method_step_3':request.form.get('method_step_3'),
        'method_step_4':request.form.get('method_step_4'),
        'method_step_5':request.form.get('method_step_5'),
        'method_step_6':request.form.get('method_step_6'),
        'method_step_7':request.form.get('method_step_7'),
        'method_step_8':request.form.get('method_step_8'),
        'method_step_9':request.form.get('method_step_9'),
        'method_step_10':request.form.get('method_step_10'),
        'like_rating':request.form.get('like_rating')
    })
    return redirect(url_for('get_recipe'))







if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=(os.environ.get('PORT')),
        debug=True)
