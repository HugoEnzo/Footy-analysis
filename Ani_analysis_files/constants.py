{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b94997aa-4426-46fe-8f9f-f8f2622a8de6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#[\n",
    "#        \"Non-Penalty Goals\", \"Assists\", \"Shots on target %\",\n",
    "#        \"Shot-Creating Actions\",\n",
    "#        \"Pass Completion %\", \"Progressive Passes\", \"Progressive Carries\",\n",
    "#        \"Passes into Final Third\", \"Touches\",\n",
    "#        \"Interceptions\", \"Tackles Won\",\n",
    "#        \"Successful Pressure %\", \"Ball Recoveries\", \"% of Aerials Won\"\n",
    "#    ]\n",
    "MIDFIELDERS = [2, 1, 14, 72, 28, 46, 124, 43, 109, 105, 87, 97, 145, 148]\n",
    "MIDFIELDERS_ATTACK = 4\n",
    "MIDFIELDERS_POSSESSION = 5\n",
    "MIDFIELDERS_DEFENSE = 5\n",
    "\n",
    "#[\n",
    "#        \"Non-Penalty Goals\", \"xA\", \"Shots on target %\",\n",
    "#        \"Shot-Creating Actions\", \"Crosses into Penalty Area\", \"Passes Received %\", \"% of Aerials Won\",\n",
    "#        \"Pass Completion %\", \"Passes into Penalty Area\", \"Touches (Att Pen)\", \n",
    "#        \"Tackles (Att 3rd)\", \"Pressures (Att 3rd)\"\n",
    "#    ]\n",
    "FORWARDS = [2, 9, 14, 72, 45, 131, 148, 28, 44, 114, 90, 100]\n",
    "FORWARDS_ATTACK = 7\n",
    "FORWARDS_POSSESSION = 3\n",
    "FORWARDS_DEFENSE = 2\n",
    "\n",
    "#[\n",
    "#        \"Non-Penalty Goals\", \"xA\", \n",
    "#        \"Pass Completion %\", \"Progressive Passes\", \"Passes into Final Third\", \"Switches\",\n",
    "#        \"% of Aerials Won\", \"Ball Recoveries\", \"Successful Pressure %\", \"Interceptions\", \"Blocks\", \"Tackles Won\", \"% of dribblers tackled\"\n",
    "#    ]\n",
    "CENTERBACKS = [2, 9, 28, 46, 43, 53, 148, 145, 97, 105, 101, 87, 93]\n",
    "CENTERBACKS_ATTACK = 2\n",
    "CENTERBACKS_POSSESSION = 4\n",
    "CENTERBACKS_DEFENSE = 7\n",
    "\n",
    "#[\n",
    "#        \"Non-Penalty Goals\", \"xA\", \"Shot-Creating Actions\", \"% of Aerials Won\", \"Carries into Penalty Area\", \"Shots on target %\"\n",
    "#        \"Pass Completion %\", \"Key Passes\", \"Passes into Final Third\", \"Touches\", \"Crosses into Penalty Area\",\n",
    "#        \"Pressures (Mid 3rd)\", \"Tackles (Mid 3rd)\", \"Interceptions\"\n",
    "#    ]\n",
    "WINGERS = [2, 9, 72, 148, 126, 14, 28, 42, 43, 109, 45, 99, 89, 105]\n",
    "WINGERS_ATTACK = 6\n",
    "WINGERS_POSSESSION = 5\n",
    "WINGERS_DEFENSE = 3\n",
    "\n",
    "#[\n",
    "#        \"Non-Penalty Goals\", \"xA\", \"Shot-Creating Actions\", \"Carries into Final Third\",\n",
    "#        \"Key Passes\",  \"Progressive Passes\", \"Passes Completed\", \"Crosses\",\n",
    "#        \"Successful Pressure %\", \"Interceptions\", \"Tackles Won\", \"Blocks\", \"Ball Recoveries\"\n",
    "#    ]\n",
    "FULLBACKS = [2, 9, 72, 125, 42, 46, 26, 54, 97, 105, 87, 101, 145]\n",
    "FULLBACKS_ATTACK = 4\n",
    "FULLBACKS_POSSESSION = 4\n",
    "FULLBACKS_DEFENSE = 5"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
