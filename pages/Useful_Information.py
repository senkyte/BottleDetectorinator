import streamlit as st
# This entire code is written by Lee Rey Jien
st.title("Useful Information")
st.write("""Recycling rates in the world remain very low due to a lack of
awareness and reluctance to carry out these practices. Here are some
information to educate you about the recycling situation in different
countries and what are the recyclable and non-recyclable items, unique
to each country.
""")

with st.expander("Singapore"):
    st.write("""Although Singapore is touted as a garden city with clean
surroundings and widespread greenery, the waste that is produced by the
populace does not match up with the immaculate image of the city. In
Singapore alone, about 900 thousand tonnes of plastic waste is discarded
and only 4 percent of the waste is recycled.

Despite efforts to educate and raise awareness on what is suitable for
recycling and what is not, some people still do not fully know about
the types of recyclable items. Here are some recyclable and non-recyclable
items:

Plastics
-----------------------
Recyclable:
- Cardboard Boxes
- Outer Packaging and Tissue Boxes
- Egg Trays
- Envelopes and Flyers
- Toilet Paper and Paper Towel Rolls
- Newspapers, Magazines and Books

(Plastics like beverage and detergent bottles, plastic bags and film
packaging can be recycled if clean.)

-----------------------
Non-Recyclable:
- Paper Towels and Tissues
- Disposable Food and Drink Packaging

(These items are often contaminated and not suitable for recycling)
- Glitter Paper
- Crayon Drawings

Glass
-----------------------
Recyclable:
- Liquor Bottles
- Drink Bottles
- Perfume, Cosmetics and Medicine Bottles
- Food and Condiment Jars
- Drinking and Wine Glasses
(Ensure that they are free of contamination)
-----------------------
Non-Recyclable:
- Oven-Safe Food Containers
- Pyrex Glassware
- Tempered Glass
- Crystal Glass
- Mirror
- Glass with Metal Wires

Metals
-----------------------
Recyclable:
- Beverage Cans
- Biscuit Tins
- Metal Containers
- Food Cans
- Paint Cans
- Old medals
-----------------------
Non-Recyclable:
- Rusty metal cans
- Dirty aluminium foil and trays
- E-waste (non-recyclable for general recycling bins)

These are the general categories of items for recycling in Singapore but there
are its exceptions.
""")

with st.expander("Malaysia"):
    st.write("""Similarly, the recycling culture in Malaysia is poor. It should
be noted that the government of Malaysia is aiming to reach a 40% recycling rate
by 2025.
""")

with st.expander("Japan"):
    st.write("""Japan has a very strong recycling culture that lends to its
clean image. The recycling of plastic bottles and packaging is enforced by the
government through the Container and Packaging Recycling Act. Almost 85 percent
of all plastic bottles are recycled.

However, these rates only apply to plastic items. Japan's overall recycling rate
is low, with glass and paper being recycled less. In 2020, the overall recycling
rate reached only 20%.
""")

with st.expander("China"):
    st.write("""China has traditionally been the centre for recycling until
2017-2018, where Operation National Sword was implemented. Due to the amount of
contaminated waste that is being transported to China, the government stopped
the import of plastics for recycling.

As the world's capital for recycling, recycling habits and lifestyles are still
not yet ingrained into the mindsets of the Chinese people. However, there are
efforts that are taken like implementing a domestic waste sorting system for
Shanghai where residents sort their waste into four categories: wet garbage,
dry garbage, recyclable waste and hazardous waste.
""")
