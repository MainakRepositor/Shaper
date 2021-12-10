import streamlit as st


def main():
	st.title("*SHAPER*")

	activity = ['Design','About',]
	choice = st.sidebar.selectbox("Select Activity",activity)

	if choice == 'Design':
		st.subheader("Design your shape 🔷")
		bgcolor2 = st.sidebar.color_picker("Pick a Bckground color")
		height = st.sidebar.slider('Height Size',50,2000,500)
		width = st.sidebar.slider("Width Size",50,2000,500)
		# border = st.slider("Border Radius",10,60,10)
		top_left_border = st.sidebar.number_input('Top Left Border',10,50,10)
		top_right_border = st.sidebar.number_input('Top Right Border',10,50,10)
		bottom_left_border = st.sidebar.number_input('Bottom Left Border',10,50,10)
		bottom_right_border = st.sidebar.number_input('Bottom Right Border',10,50,10)

		border_style = st.sidebar.selectbox("Border Style",["dotted","dashed","solid","double","groove","ridge","inset","outset","none","hidden"])
		border_color = st.sidebar.color_picker("Pick a Border Color","#654FEF")
	   

		html_design = """
		<div style="
        height:{}px;
        width:{}px;
        background-color:{};
        border-radius:{}px {}px {}px {}px;
        border-style:{};
        border-color:{}">
		</div>
        <br>
		"""
         
		st.markdown(html_design.format(height,width,bgcolor2,top_left_border,top_right_border,bottom_left_border,bottom_right_border,border_style,border_color),unsafe_allow_html=True)
       
		if st.checkbox("View Code"):
			st.subheader("Code")
			result_of_design = html_design.format(height,width,bgcolor2,top_left_border,top_right_border,bottom_left_border,bottom_right_border,border_style,border_color)	
                		
			st.code(result_of_design)

	if choice =="About":
		st.subheader("About Shaper")
		st.markdown('''*Shaper is a free CSS shape building tool built using Streamlit. Shaper is used to build customized shapes using CSS. The CSS codes are also displayed for the user. Any user can simply copy and paste the code in their HTML pages to achieve the required shape with the required dimensions on their webpage.*''')
		st.success("Made By : [Mainak Chaudhuri](https://www.linkedin.com/in/mainak-chaudhuri-127898176/)")
		



if __name__ == '__main__':
	main()
