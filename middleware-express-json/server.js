
import express from "express";

const app=express();
app.use(express.json());

const port=3000

app.use((req, res, next) => {
  console.log("Request received");
  next();
});

//Middleware #۱:
app.use((req,res,next)=>{
    const usernameHeader=req.headers["x-username"];
    req.username=usernameHeader ? usernameHeader : null;
    next();
});



// Middleware #3: validate body
function validateBodyArray(req,res,next){
    if (!Array.isArray(req.body)) {
        return res.status(400).send("JSON must be an array");
    }

    const allStrings=req.body.every(item=>typeof(item)==='string');
    if (!allStrings){
        return res.status(400).send("All elements in array must be strings");
        
    }

    next();
}

app.post('/',validateBodyArray,(req,res)=>{
    const usernamePart = req.username
      ? `You are authenticated as ${req.username}.`
      : `You are not authenticated.`;

    const subjectsCount = req.body.length;
    const subjectsList = req.body.join(", ");
    const subjectsPart = `You have requested information about ${subjectsCount} subject${subjectsCount !== 1 ? "s" : ""}: ${subjectsList}.`;  

   res.send(`${usernamePart}\n\n${subjectsPart}`);
})

app.listen(port, () => {
  console.log("Express middleware server running on port 3000");
});

app.listen(port,()=>{
    console.log(`Server running on port ${port}`);
});