import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Libron - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        color: #2e86ab;
        border-bottom: 2px solid #2e86ab;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .project-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .skill-bar {
        background-color: #e0e0e0;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .skill-fill {
        background-color: #1f77b4;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 10px;
        text-align: right;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Sidebar
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Autobiography", "Portfolio", "Skills", "Contact"])
    
    st.markdown("---")
    st.header("Quick Info")
    st.markdown("**Location:** Talisay City, Cebu")
    st.markdown("**Email:** libron.christianneil@gmail.com")
    st.markdown("**Phone:** +63 912 345 6789")
    
    st.markdown("---")
    st.header("Social Links")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Libron-ChristianNeil)")
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.facebook.com/christianneil.libron/)")

# Home Page
if page == "Home":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://raw.githubusercontent.com/Libron-ChristianNeil/assets/main/profile.JPG",
                 width=300, caption="Christian Neil Libron - Data Scientist & Developer")
    
    with col2:
        st.markdown('<div class="main-header">Christian Neil Libron</div>', unsafe_allow_html=True)
        st.markdown("### Data Scientist & Developer")
        st.markdown("---")
        st.markdown("""
        Welcome to my personal portfolio! I'm a passionate and driven 3rd year Computer Science student at 
        Cebu Institute of Technology - University. Currently pursuing my Bachelor of Science in Computer Science, 
        I'm actively developing my skills in software development, data structures, and algorithms. I'm enthusiastic 
        about exploring various technologies and building practical solutions while continuously learning and growing in the 
        field of computer science.
        """)
        
        # Metrics
        col4, col5, col6 = st.columns(3)
        with col4:
            st.metric("Projects Completed", "20+", "5")
        with col5:
            st.metric("Clients Served", "5+", "3")
        with col6:
            st.metric("Certifications", "7", "1")
    
    # Recent Activity
    st.markdown('<div class="section-header">Recent Activity</div>', unsafe_allow_html=True)
    
    timeline_data = pd.DataFrame({
        'Date': pd.date_range('2023-01-01', periods=12, freq='M'),
        'Projects': [2, 3, 1, 4, 2, 3, 5, 2, 4, 3, 2, 4],
        'Blog Posts': [1, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1, 3]
    })
    
    fig = px.line(timeline_data, x='Date', y=['Projects', 'Blog Posts'], 
                  title='Monthly Activity Overview')
    st.plotly_chart(fig, use_container_width=True)

# Autobiography Page
elif page == "Autobiography":
    st.markdown('<div class="main-header">My Journey</div>', unsafe_allow_html=True)
    
    # Timeline
    st.markdown('<div class="section-header">My Journey</div>', unsafe_allow_html=True)

    timeline_events = [
        {"year": "2023", "event": "Started BS Computer Science at CIT-U", "description": "Began my journey in computer science at Cebu Institute of Technology - University"},
        {"year": "2023", "event": "First Programming Projects", "description": "Completed introductory programming courses and built my first simple applications"},
        {"year": "2024", "event": "Data Structures & Algorithms", "description": "Deepened understanding of core CS concepts and started working on more complex projects"},
        {"year": "2025", "event": "Mobile Development & Database Courses", "description": "Learned full-stack development and database management systems"},
        {"year": "2025", "event": "Automata Theory and Formal Languages", "description": "Exploring specialized fields and preparing for internship opportunities"}
    ]

    for event in timeline_events:
        with st.expander(f"{event['year']} - {event['event']}"):
            st.write(event['description'])

    # Personal Story
    st.markdown('<div class="section-header">My Story</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Academic Journey
        My passion for technology began when I first discovered programming during my senior high school years. 
        The ability to create solutions through code fascinated me and led me to pursue Computer Science at 
        Cebu Institute of Technology - University.
        
        Throughout my academic journey, I've been actively building my foundation in software development, 
        data structures, and problem-solving while maintaining a strong academic record.
        """)

    with col2:
        st.markdown("""
        ### Growth & Aspirations
        As I progress through my degree, I'm continuously expanding my technical skills through coursework, 
        personal projects, and self-study. I'm particularly interested in web development, data science, 
        and mobile application development.
        
        I believe in hands-on learning and am always seeking opportunities to apply classroom knowledge 
        to real-world problems through projects and upcoming internship opportunities.
        """)
        
    # Education
    st.markdown('<div class="section-header">Education & Certifications</div>', unsafe_allow_html=True)
        
    education_data = {
        "Degree": ["BS Computer Science", "C Certification", "Java Certification"],
        "Institution": ["CIT-U", "CodeChum", "CodeChum"],
        "Year": ["2023", "2024", "2025"],
    }
        
    st.table(pd.DataFrame(education_data))


# Portfolio Page
elif page == "Portfolio":
    st.markdown('<div class="main-header">My Portfolio</div>', unsafe_allow_html=True)
    
    # Project filters
    col1, col2, col3 = st.columns(3)
    with col1:
        category_filter = st.selectbox("Filter by Category", ["All", "Image Processing", "Web Development", "Mobile Apps", "Utilities", "Academic Projects"])
    with col2:
        tech_filter = st.selectbox("Filter by Technology", ["All", "Python", "Java", "JavaScript", "C++", "React"])
    with col3:
        year_filter = st.slider("Project Year", 2022, 2024, (2022, 2024))
    

    st.markdown("""
    <style>
    .project-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        border-left: 5px solid #1f77b4;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .project-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    /* Remove extra spacing from streamlit elements */
    .stContainer {
        padding: 0 !important;
        margin: 0 !important;
    }
    div[data-testid="column"] {
        padding-top: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Projects data
    projects = [
        {
            "title": "Image Processing Application",
            "category": "Image Processing",
            "technology": "Python",
            "year": 2024,
            "description": "A comprehensive image processing application with filters, transformations, and effects built using Python and OpenCV",
            "image": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "github_url": "https://github.com/Libron-ChristianNeil/LIBRON_ImageProcessing.git",
            "status": "Completed"
        },
        {
            "title": "Calculator Application",
            "category": "Utilities",
            "technology": "Java",
            "year": 2023,
            "description": "A fully functional calculator application with basic and scientific operations, featuring a clean GUI interface",
            "image": "https://images.unsplash.com/photo-1587145820266-a5951ee6f620?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "github_url": "https://github.com/Libron-ChristianNeil/LIBRON_Calculator.git",
            "status": "Completed"
        },
        {
            "title": "Student Management System",
            "category": "Web Development",
            "technology": "JavaScript",
            "year": 2024,
            "description": "A web-based student management system for tracking academic records, grades, and attendance with admin dashboard",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "github_url": "#",
            "status": "In Progress"
        },
        {
            "title": "E-Learning Mobile App",
            "category": "Mobile Apps",
            "technology": "React",
            "year": 2023,
            "description": "Cross-platform mobile application for online learning with video lectures, quizzes, and progress tracking",
            "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "github_url": "#",
            "status": "Completed"
        },
        {
            "title": "Data Structures Visualizer",
            "category": "Academic Projects",
            "technology": "C++",
            "year": 2023,
            "description": "Interactive visualization tool for common data structures (trees, graphs, sorting algorithms) with step-by-step execution",
            "image": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "github_url": "#",
            "status": "Completed"
        }
    ]
    
    # Filter projects
    filtered_projects = projects
    if category_filter != "All":
        filtered_projects = [p for p in filtered_projects if p["category"] == category_filter]
    if tech_filter != "All":
        filtered_projects = [p for p in filtered_projects if p["technology"] == tech_filter]
    filtered_projects = [p for p in filtered_projects if year_filter[0] <= p["year"] <= year_filter[1]]
    
    if 'expanded_project' not in st.session_state:
        st.session_state.expanded_project = None
    
    for i, project in enumerate(filtered_projects):

        # Project card
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(
                project["image"], 
                use_container_width=True,
                caption=project["title"]
            )
        
        with col2:
            st.subheader(project["title"])
            
            # Project metadata
            meta_col1, meta_col2, meta_col3 = st.columns(3)
            with meta_col1:
                st.write(f"**Category:** {project['category']}")
            with meta_col2:
                st.write(f"**Technology:** {project['technology']}")
            with meta_col3:
                st.write(f"**Year:** {project['year']}")
            
            st.write(project["description"])
            
            # Status
            if project["status"] == "Completed":
                st.success(f"Status: {project['status']}")
            else:
                st.warning(f"Status: {project['status']}")
            
            # Action buttons
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                # Toggle expander for this specific project
                if st.button("View Details", key=f"view_{i}"):
                    if st.session_state.expanded_project == i:
                        st.session_state.expanded_project = None
                    else:
                        st.session_state.expanded_project = i
                    st.rerun()
            with btn_col2:
                if project["github_url"] != "#":
                    st.markdown(f"[📁 GitHub Repository]({project['github_url']})", unsafe_allow_html=True)
                else:
                    st.info("GitHub: Coming Soon")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Show expander right after the project card if this project is expanded
        if st.session_state.expanded_project == i:
            with st.expander(f"📋 Detailed View: {project['title']}", expanded=True):
                st.write(f"**Full Description:** {project['description']}")
                st.write(f"**Technology Stack:** {project['technology']}")
                st.write(f"**Project Category:** {project['category']}")
                st.write(f"**Year Developed:** {project['year']}")
                st.write(f"**Current Status:** {project['status']}")
                
                if project["github_url"] != "#":
                    st.markdown(f"**🔗 GitHub Repository:** [{project['github_url']}]({project['github_url']})")
                else:
                    st.write("**GitHub Repository:** Coming soon!")
                
                # Close button
                if st.button("Close Details", key=f"close_{i}"):
                    st.session_state.expanded_project = None
                    st.rerun()


# Skills Page
elif page == "Skills":
    st.markdown('<div class="main-header">Skills & Expertise</div>', unsafe_allow_html=True)
    
    # Technical Skills
    st.markdown('<div class="section-header">Technical Skills</div>', unsafe_allow_html=True)
    
    skills = {
        "Python": 95,
        "JavaScript": 85,
        "SQL": 90,
        "React": 80,
        "TensorFlow": 75,
        "AWS": 70,
        "Docker": 65,
        "Git": 95
    }
    
    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.markdown(f"""
        <div class="skill-bar">
            <div class="skill-fill" style="width: {level}%">{level}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills Radar Chart
    st.markdown('<div class="section-header">Skills Overview</div>', unsafe_allow_html=True)
    
    categories = ['Programming', 'Data Analysis', 'Web Dev', 'ML/AI', 'Cloud', 'DevOps']
    values = [90, 85, 80, 75, 70, 65]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skill Level'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tools & Technologies
    st.markdown('<div class="section-header">Tools & Technologies</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Data Science**")
        st.markdown("- Pandas, NumPy, Scikit-learn")
        st.markdown("- Jupyter, Colab")
        st.markdown("- Tableau, Power BI")
    
    with col2:
        st.markdown("**Web Development**")
        st.markdown("- React, Node.js, Express")
        st.markdown("- Django, Flask")
        st.markdown("- HTML5, CSS3, Bootstrap")
    
    with col3:
        st.markdown("**DevOps & Cloud**")
        st.markdown("- AWS, Azure, GCP")
        st.markdown("- Docker, Kubernetes")
        st.markdown("- CI/CD, Jenkins")

# Contact Page
elif page == "Contact":
    st.markdown('<div class="main-header">Get In Touch</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="section-header">Send Me a Message</div>', unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.selectbox("Subject", [
                "Project Inquiry", 
                "Job Opportunity", 
                "Collaboration", 
                "General Question"
            ])
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            if submitted:
                if name and email and message:
                    st.success("Thank you for your message! I'll get back to you soon.")
                else:
                    st.error("Please fill in all required fields.")
    
    with col2:
        st.markdown('<div class="section-header">Contact Info</div>', unsafe_allow_html=True)
        
        st.markdown("""
        **📍 Address**  
        Lawaan  
        Talisay City, Cebu 6045
        
        **📧 Email**  
        libron.christianneil@gmail.com
        
        **📞 Phone**  
        +63 912 345 6789
        
        **🌐 Website**  
        www.libronchristianneilportfolio.com
        """)
        
        st.markdown("---")
        st.markdown("### Let's Connect")
        
        social_options = ["LinkedIn", "GitHub", "Twitter", "Instagram"]
        selected_social = st.selectbox("Follow me on", social_options)
        
        if st.button("Visit Profile"):
            st.info(f"Opening {selected_social} profile...")
    
    # Map
    st.markdown('<div class="section-header">Location</div>', unsafe_allow_html=True)
    
    # Sample map data 
    map_data = pd.DataFrame({
        'lat': [10.2447, 10.2600, 10.2300, 10.2500],
        'lon': [123.8494, 123.8600, 123.8400, 123.8500]
    })

    st.map(map_data, zoom=12)