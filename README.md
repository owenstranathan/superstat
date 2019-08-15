# Superstat

Because I've been working in windows a lot lately and can't seem to use batch properly I had to write a few lines of python.
And usually someone elses solution is super suck. (and or too much shit)

## Usage

```
D:\code> dir
 Volume in drive D is Storage
 Volume Serial Number is 285E-3F21

 Directory of D:\code

08/13/2019  10:42 PM    <DIR>          .
08/13/2019  10:42 PM    <DIR>          ..
08/09/2019  12:49 PM    <DIR>          erincatto
08/09/2019  12:49 PM    <DIR>          glfw
08/09/2019  12:49 PM    <DIR>          microsoft
08/13/2019  10:41 PM    <DIR>          owenstranathan
08/09/2019  12:47 PM    <DIR>          pixijs
08/13/2019  09:10 PM    <DIR>          scratch
08/09/2019  12:47 PM    <DIR>          SFML
08/09/2019  12:48 PM    <DIR>          vim
08/13/2019  11:18 AM    <DIR>          wabisoft
               0 File(s)              0 bytes
              11 Dir(s)  855,300,739,072 bytes free
D:\code> superstat
 D:\code\owenstranathan\DeadManDodgeball2D
         7 files changed, 81 insertions(+), 38 deletions(-)

 D:\code\owenstranathan\particles
         2 files changed, 1 insertion(+), 31 deletions(-)

 D:\code\owenstranathan\pipenv.zsh
         1 file changed, 7 insertions(+), 2 deletions(-)

 D:\code\owenstranathan\superstat
         1 file changed, 1 insertion(+), 1 deletion(-)

 D:\code\owenstranathan\todo
         1 file changed, 4 insertions(+)

 D:\code\owenstranathan\vimfiles
         2 files changed, 0 insertions(+), 0 deletions(-)

 D:\code\owenstranathan\waves
         12 files changed, 94 insertions(+), 80 deletions(-)

 D:\code\wabisoft\waves
         1 file changed, 1 insertion(+)
```

## Installation

Clone this repo somewhere

```
D:\code> mkdir owenstranatha
D:\code>git clone https://github.com/owenstranathan/superstat.git owenstranathan/superstat
```

then add that directory to your Path

1. press windows key
2. type "path"
3. click "Edit the system environment variables"
4. click the butten labeled "Environment Variables..."
5. Under "User variables for USER", double click "Path"
6. Click "New"
7. In the text field that appears enter the path you cloned superstat to (in my case `D:\code\owenstranathan\superstat`)
