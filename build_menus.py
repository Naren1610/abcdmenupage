import os
import re

def mk_item(name, price, desc, veg=False, spicy=False):
    markers = ""
    if veg: markers += '<span class="indicator veg" title="Vegetarian">V</span> '
    if spicy: markers += '<span class="indicator spicy" title="Spicy">S</span> '
    return f'''
        <article class="menu-item-card scroll-reveal">
            <div class="item-header">
                <div class="item-name-group">
                    {markers}<h4 class="item-name">{name.strip()}</h4>
                </div>
                <div class="item-leader"></div>
                <span class="item-price">{price.strip()}</span>
            </div>
            <p class="item-desc">{desc.strip()}</p>
        </article>'''

appetizers = """
<section class="menu-section">
    <h3 class="menu-category-title">The Imperial Tandoor</h3>
    <p class="menu-category-subtitle">Flame-charred legacies</p>
    <div class="menu-grid">
"""
appetizers += mk_item("Maharaja Prawns", "21.59", "Tiger prawns infused with citrus and House special Tandoori essence, kissed by fire for a perfect balance of heat, aroma, and oceanic sweetness.")
appetizers += mk_item("Pesto Shrimp Emeraldo", "23.59", "Succulent Jumbo marinated in a vibrant basil pesto, kissed by the tandoor flame for a smoky, aromatic finish.")
appetizers += mk_item("Royal Seekh of Kheema", "19.59", "Hand-crafted lamb skewers blended with our heirloom spices, cooked over glowing flames to create a delicately smoky, melt-in-mouth experience.")
appetizers += mk_item("Classic Tandoori Chicken", "18.59", "Succulent bone-in chicken infused with a secret heritage spice blend, roasted to tender perfection, with a smoky aroma that lingers in every bite.")
appetizers += mk_item("Crimson Kashmiri Murgh Tikka", "18.59", "Chicken marinated for 24 hours in a rich Kashmiri chili-spice symphony, then flame-seared for a fiery, jewel-toned finish.")
appetizers += mk_item("Malai Silk Murgh Kebab", "19.59", "Velvety morsels of chicken enriched with cream, green chili, and cardamom, kissed with subtle smoke, melting on the palate with every bite.")
appetizers += mk_item("Achaari Charred Wings", "18.59", "Orchard-raised wings marinated in bold pickling spices, crisped over embers to deliver a tangy, smoky, and deeply flavorful bite.", spicy=True)
appetizers += mk_item("Artisan Ember Paneer", "17.59", "House-pressed paneer steaks enriched with a medley of spices, charred to perfection with a subtle smoky finish, paired with roasted bell peppers.", veg=True)
appetizers += mk_item("Verdant Hariyali Paneer", "18.59", "Paneer enveloped in a vibrant blend of fresh mint, spinach, and toasted spices, offering a bright, herbaceous, and indulgent flavor experience.", veg=True)
appetizers += mk_item("Charred Soya Chaap", "17.59", "Tender batons of delhi waala Soya chaap warmly slept in in our house special marinade, and then slowly grilled & charred in tandoor to achieve a charred exterior and succulent bite.", veg=True)
appetizers += """
    </div>
</section>
<section class="menu-section">
    <h3 class="menu-category-title">Dragon & Spice</h3>
    <p class="menu-category-subtitle">A vibrant journey blending the bold spices of India with wok-fired flavors</p>
    <div class="menu-grid">
"""
appetizers += mk_item("Veg Manchurian", "14.59", "Crisp vegetable balls tossed in a mildly spicy soy-garlic sauce.", veg=True)
appetizers += mk_item("Gobi Manchurian", "14.59", "Cauliflower florets fried and coated in tangy Indo-Chinese sauce.", veg=True)
appetizers += mk_item("Chilli Paneer", "15.99", "Soft paneer cubes sautéed with capsicum, onion, and tangy chili sauce.", veg=True, spicy=True)
appetizers += mk_item("Honey Chilli Potato", "15.99", "Crispy potato fingers tossed in sweet and spicy glaze.", veg=True)
appetizers += mk_item("Hyderabadi Chicken 65", "16.59", "South-Indian style fried chicken with bold masala and curry leaf tempering.", spicy=True)
appetizers += mk_item("Chilli Chicken", "16.59", "Juicy chicken pieces tossed with bell peppers and spicy Indo-Chinese sauce.", spicy=True)
appetizers += mk_item("Chicken Majestic", "17.59", "Tender chicken cooked with garlic, chili, and light soy sauce.")
appetizers += mk_item("Chicken Lollipops (Wet)", "17.59", "Crispy chicken wings coated in a glossy, spicy sauce.")
appetizers += mk_item("Drums of Heaven", "17.59", "Crispy chicken drumettes served with house-made honey-chili glaze.")
appetizers += mk_item("Apollo Fish", "17.59", "Lightly fried fish in tangy sweet and sour sauce.")
appetizers += mk_item("Dragon Chicken", "16.99", "Wok-tossed chicken with chili, garlic, and hint of sesame.", spicy=True)
appetizers += """
    </div>
</section>
"""

curries = """
<section class="menu-section">
    <h3 class="menu-category-title">Anantha Shakhahaari</h3>
    <p class="menu-category-subtitle">Vegetarian Elegance</p>
    <div class="menu-grid">
"""
curries += mk_item("Makhanwala Paneer Butter Masala", "16.99", "Soft paneer cubes enveloped in a luscious tomato-butter sauce, finished with cream and delicate Indian spices.", veg=True)
curries += mk_item("Paneer Tikka Masala", "16.99", "Char-grilled paneer simmered in a fragrant onion-tomato masala, kissed with subtle smokiness.", veg=True)
curries += mk_item("Paneer Lababdar", "16.99", "Paneer cubes in a rich velvety, buttery gravy with aromatic spices and a hint of cream.", veg=True)
curries += mk_item("Palak Paneer", "16.99", "Fresh spinach purée cooked with paneer cubes, lightly tempered with garlic and cumin.", veg=True)
curries += mk_item("Malai Kofta", "17.99", "Pillowy dumplings of paneer and seasonal vegetables, floating in our lovely creamy secret spice infused, riped tomato gravy.", veg=True)
curries += mk_item("Sarson Ka Saag", "16.99", "Slow-cooked mustard greens with a balance of spices, rustic and comforting.", veg=True)
curries += mk_item("Mushroom Do Pyaza", "16.99", "Mushrooms sautéed with layers of onions and traditional masala.", veg=True)
curries += mk_item("Mix Veg Jalfrezi", "16.99", "Seasonal vegetables sautéed with peppers and onions in a tangy tomato masala.", veg=True)
curries += mk_item("Dal Makhani", "16.99", "Black lentils and kidney beans slow cooked with butter and cream for rich flavor.", veg=True)
curries += mk_item("Dhaaba waala Tadka Dal", "15.99", "Yellow lentils tempered with cumin, garlic, and mild spices. This is simple, but taste our recipe and go crazy!", veg=True)
curries += mk_item("Punjabi Chole", "16.99", "Chickpeas cooked with earthy, aromatic masalas to deliver robust and traditional flavor with every bite.", veg=True)
curries += mk_item("Kadhi Pakora", "16.99", "Gram flour fritters simmered in yogurt-based curry with light tempering.", veg=True)
curries += """
    </div>
</section>
<section class="menu-section">
    <h3 class="menu-category-title">The Mamsa Rasoi</h3>
    <p class="menu-category-subtitle">Non-Vegetarian Mastery</p>
    <div class="menu-grid">
"""
price = "19.99"
curries += mk_item("Rogan Josh", price, "Mutton cooked in yogurt and Kashmiri red chili gravy for gentle warmth.")
curries += mk_item("Lal Maas", price, "Traditional fiery mutton curry prepared with secret chilies.", spicy=True)
curries += mk_item("Telangana Dhaavath Mutton Curry", price, "Rustic, slow-cooked mutton infused with the region’s signature bold spices and aromatic undertones.", spicy=True)
curries += mk_item("Munakkaya Mutton", price, "Mutton and drumstick pods in a lightly spiced, hearty gravy, offering layered flavors and depth.")
curries += mk_item("Mutton Vindaloo", price, "Tangy Goan-style curry with a gentle heat, balancing spices and vinegar notes for a bold yet refined taste.", spicy=True)
curries += mk_item("Saag Gosht", price, "Succulent mutton slow-cooked with fresh spinach, delivering an earthy, aromatic, and tender curry.")
curries += mk_item("Nilgiri Lamb Kofta", price, "Hand-rolled lamb dumplings in our signature spiced green herb sauce, delicate yet flavorful.")
curries += mk_item("Kheema Matar", "19.99", "Minced mutton cooked with peas in lightly spiced masala.")
curries += mk_item("Kheema Mutti Curry", "19.99", "Home made kheema balls, served in our aromatic southern spiced sauce.")

curries += mk_item("Goan Prawn Curry", "22.99", "Prawns simmered in coconut-tamarind coastal gravy.")
curries += mk_item("Royyala Iguru", "22.99", "Semi-dry prawns cooked with curry leaves and mild chili.")

curries += mk_item("Goan Fish Curry", "21.99", "Fresh fish cooked in tangy coconut-based gravy.")
curries += mk_item("Chepala Pulusu", "21.99", "Tamarind fish stew with subtle South Indian spices.")

curries += mk_item("Punjabi Dhaaba waala Anda Masala", "16.99", "Boiled eggs simmered in light onion-tomato masala.")

price = "17.99"
curries += mk_item("Delhi Waala Butter Chicken", price, "Tandoor-roasted chicken in a tomato-butter gravy with mild spices.")
curries += mk_item("Kolhapuri Chicken", price, "Chicken cooked with lightly roasted Kolhapuri masala.", spicy=True)
curries += mk_item("Chicken Do Pyaza", price, "Chicken cooked with layers of onions in a simple masala.")
curries += mk_item("Chicken Korma", price, "Chicken in mild yogurt and nut-based sauce.")
curries += mk_item("Chicken Tikka Masala", price, "Grilled chicken in spiced tomato-onion masala.")
curries += mk_item("Chicken Vindaloo", price, "Spicy and tangy Goan chicken curry.", spicy=True)
curries += mk_item("Andhra Home made Chicken Curry", price, "Bone-In Chicken cooked with regional spices for balanced heat.", spicy=True)
curries += mk_item("Ginger Chicken", price, "Old Hyderabadi waala Chicken simmered in a crazy gravy of fresh ginger, green chili.")
curries += mk_item("Hyderabadi Dum Chicken", price, "Slow-cooked chicken sealed with aromatic spices.")
curries += mk_item("Orissa Dhaaba Style Rambha Chicken", price, "Regional-style chicken curry with secret sauce and spices.")

curries += """
    </div>
</section>
<section class="menu-section">
    <h3 class="menu-category-title">Rice & Noodles</h3>
    <p class="menu-category-subtitle"> Custom House Veggies (+1) / Egg (+2) / Chicken (+3) / Prawn (+4)/ Mixed(+5)</p>
    <div class="menu-grid">
"""
curries += mk_item("Wok fired Soft Noodles", "14.59", "Classic stir-fried noodles with vegetables and light soy seasoning.")
curries += mk_item("Schezwan Noodles", "15.59", "Spicy noodles with a bold, exotic Sichuan peppers schezwan sauce.", spicy=True)
curries += mk_item("Singapore Noodles", "16.59", "Thin rice noodles stir-fried with curry-flavored vegetables and protein of choice.")
curries += mk_item("Pad Thai", "16.59", "Rice noodles tossed with egg, vegetables, and tamarind-infused sauce.")
curries += mk_item("Flamed & Tossed Fried Rice", "14.59", "Fragrant rice stir-fried with vegetables and house made seasonings.")
curries += mk_item("Schezwan Fried Rice", "15.59", "Lightly spice Rice with a twist of our house made schezwan sauce.", spicy=True)
curries += mk_item("Chilli Garlic Fried Rice", "15.59", "An amalgamation of our Chilli & garlic into the flame burnt wok with granular rice.", spicy=True)
curries += """
    </div>
</section>
"""

biryani = """
<section class="menu-section">
    <h3 class="menu-category-title">Murali Ka Zaikha</h3>
    <p class="menu-category-subtitle">The Royal Tradition</p>
    <div class="menu-grid">
"""
biryani += mk_item("Hyderabadi Chicken Dum Biryani", "17.59", "Fragrant basmati rice layered with marinated chicken, slow-cooked in the traditional Dum style with exotic herbs and saffron.")
biryani += mk_item("Hyderabadi Mutton Dum Biryani", "19.59", "Tender mutton pieces marinated overnight in yogurt and spices, layered with basmati rice and slow-cooked to perfection.")
biryani += mk_item("Veg Dum Biryani", "16.59", "A medley of fresh vegetables and paneer layered with aromatic basmati rice and cooked on dum with subtle spices.", veg=True)
biryani += """
    </div>
</section>
<section class="menu-section">
    <h3 class="menu-category-title">Prelude Plates</h3>
    <p class="menu-category-subtitle">Devouring handcrafted recipes where traditional techniques meet contemporary expression</p>
    <div class="menu-grid">
"""
biryani += mk_item("Uff Uff Wings", "17.59", "When an enthusiastic Odiyan chilli meets the Spicy Telugu – We say Uff Uff.", spicy=True)
biryani += mk_item("Kheema Muttilu", "18.99", "Rathnamma’s Recipe - Rustic minced meat dumplings with fresh herbs, and spices, pounded together for a rich and savory bite.")
biryani += mk_item("Chettinad Mutton Sukka", "18.99", "Our Chef Bala’s creation – Slow roasted mutton, tossed in roasted spices, curry leaves, and black pepper in achieving a semi dry, intensely aromatic South Indian Classic.", spicy=True)
biryani += mk_item("Gongura Chicken Dry", "17.59", "Succulent pieces of chicken wok-tossed with tangy gongura (sorrel leaves), infused with aromatic spices, garlic, and red chilies, finished with a smoky wok flavor for an irresistible bite.", spicy=True)
biryani += mk_item("Mangalorean Pompano Fry", "22.59", "Pompano bathed in a beauty of spices, rested in its peace. Patiently grilled on our well-seasoned Cast-Iron.")
biryani += mk_item("Amritsari Fried Fish", "18.99", "Iconic Street delicacy! Fish fillets marinated in carom and gram flour-based batter with our secret essence.")
biryani += mk_item("Hyderabadi Royal Haleem", "18.59", "Basss… Khaa ke dekho! A royal delicacy slow-cooked to perfection.")
biryani += mk_item("Marag", "18.99", "Shaan bolthe hum isko! Exquisite, rich, and flavorful soup.")

biryani += """
    </div>
</section>
<section class="menu-section">
    <h3 class="menu-category-title">Artisanal Breads</h3>
    <div class="menu-grid">
"""
biryani += mk_item("Plain Naan", "3.59", "Fresh and soft clay oven baked bread.", veg=True)
biryani += mk_item("Handmade Tandoori Roti", "4.59", "Whole wheat bread baked in tandoor.", veg=True)
biryani += mk_item("Butter Naan", "4.59", "Layered flatbread slathered in butter.", veg=True)
biryani += mk_item("Laccha Paratha", "5.59", "Flaky, multi-layered whole wheat bread.", veg=True)
biryani += mk_item("Garlic Naan", "4.99", "Infused with chopped garlic and butter.", veg=True)
biryani += mk_item("Paneer Paratha", "5.59", "Stuffed with spiced Indian cottage cheese.", veg=True)
biryani += mk_item("Chilly Garlic Naan", "5.59", "Topped with spicy green chilies and garlic.", veg=True, spicy=True)
biryani += mk_item("Cheese Naan", "5.59", "Stuffed generously with melted cheese.", veg=True)
biryani += mk_item("Chilly Cheese Naan", "6.59", "Naan stuffed with spicy green chilies and melted cheese.", veg=True, spicy=True)
biryani += mk_item("Bhature", "4.59", "Fluffy deep-fried leavened sourdough bread.", veg=True)
biryani += """
    </div>
</section>
"""

desserts = """
<section class="menu-section">
    <h3 class="menu-category-title">Sweet Endings</h3>
    <p class="menu-category-subtitle">Decadent indulgence to complete your journey</p>
    <div class="menu-grid">
"""
desserts += mk_item("Saffron Malai Rasmalai", "7.99", "Pillowy cottage cheese discs soaked in sweetened, thickened milk delicately flavored with saffron and cardamom.", veg=True)
desserts += mk_item("Gulab Jamun Flambé", "6.99", "Classic warm golden dumplings resting in rose-scented syrup, served hot.", veg=True)
desserts += mk_item("Mango Pistachio Kulfi", "8.99", "Traditional dense Indian ice cream infused with Alphonso mango and crushed pistachios.", veg=True)
desserts += mk_item("Shahi Tukda", "8.99", "Royal Awadhi dessert of fried bread soaked in saffron syrup and topped with rich rabdi.", veg=True)
desserts += """
    </div>
</section>
<section class="menu-section">
    <h3 class="menu-category-title">Crafted Beverages</h3>
    <p class="menu-category-subtitle">Refreshing accompaniments</p>
    <div class="menu-grid">
"""
desserts += mk_item("Mango Lassi", "5.99", "Creamy yogurt drink blended with sweet Alphonso mangoes and a hint of cardamom.", veg=True)
desserts += mk_item("Rose Sharbat", "4.99", "Cooling rose-infused syrup stirred into chilled milk or water.", veg=True)
desserts += mk_item("Masala Chai", "3.99", "Our signature brew of black tea, ginger, cardamom, and Indian spices.", veg=True)
desserts += """
    </div>
</section>
"""

import sys
base = sys.argv[1]

for title, html in [('appetizers', appetizers), ('curries', curries), ('biryani', biryani), ('desserts', desserts)]:
    path = os.path.join(base, f"{title}.html")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace the menu-content with our generated html
    content = re.sub(r'(<div class="menu-content">).*?(</div>\s*</main>)', r'\1\n' + html + r'\n\2', content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Menus generated successfully.")
