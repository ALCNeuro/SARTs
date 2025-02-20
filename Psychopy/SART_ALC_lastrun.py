#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Thu Oct 31 16:07:20 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = '2AFC_MF_NT1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/arthurlecoz/Library/Mobile Documents/com~apple~CloudDocs/Desktop/A_Thesis/Experiments/DONE/SART_Py/SART_ALC_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 720], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='event')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='Pyglet')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "SART_Parameters" ---
    # Run 'Begin Experiment' code from SetUp_SART
    import numpy as np
    
    exp_Name = "SART_ALC_lastrun.py"
    #SART set-up for variables used in exp
    nBlock = 4
    nTrial = 24
    #duration of a block = 7min
    # durBlock = 420
    #duration of a trial between 30 and 70sec
    durTrial = [i for i in range (30,71)]
    doubledurTrial = [i for i in range (60, 141)]
    dur_Training = 27
    #duration of apparition of an image between
    # 1.00 and 1.5sec
    durImg = [i/100 for i in range (75,126)]
    
    #percentage of go vs nogo
    perGo = 0.8
    
    # Create digit list and is target or no
    go_digits = [1,2,4,5,6,7,8,9]
    nogo_digit = 3
    
    training_digits = []
    for i in range(dur_Training) :
        if i < perGo * dur_Training :
            training_digits.append(randchoice(go_digits))
        else :
            training_digits.append(nogo_digit)
    training_duration = [randchoice(durImg) for i in range(dur_Training)]
    training_order = [i for i in range(dur_Training)]
    shuffle(training_order)
    
    
    # --- Initialize components for Routine "Instru1" ---
    Instru_1 = visual.TextStim(win=win, name='Instru_1',
        text="Bienvenu-e et merci d'avoir accepté de participer à l'expérimentation !\n\nDes chiffres vont apparaître au milieu de l'écran.\n\nÀ chaque fois qu'un chiffre apparaît, appuyez sur la barre d'espace, SAUF pour le chiffre 3 !\n\nAppuyez sur la barre d'espace pour continuer...",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instru_1 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Instru_Probes" ---
    InstruProbes = visual.TextStim(win=win, name='InstruProbes',
        text="De temps en temps, vous serez interrompu afin de comprendre votre état d'esprit - juste avant l'interruption.\n\nDes réponses vous seront alors proposées \navec des chiffres avant (1., 2., ...)\n\nAppuyez alors sur la touche de votre clavier correspondant au chiffre de la réponse.\n\nAppuyez sur la barre d'espace pour continuer...",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Instru3" ---
    Instru_3 = visual.TextStim(win=win, name='Instru_3',
        text="Vous ne pouvez pas faire de pause en milieu de bloc. Je vous prie de bien vouloir attendre la fin d'un bloc. \n\nVous aurez alors la possibilité de prendre une courte pause avant de reprendre.\n\nSoyez le plus rapide et le plus précis possible! \nBonne Chance.\n\nAppuyez sur la barre d'espace pour continuer...",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instru_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Pause" ---
    PausePrep3 = visual.TextStim(win=win, name='PausePrep3',
        text='Préparez-vous à commencer\n\n3',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    PausePrep2 = visual.TextStim(win=win, name='PausePrep2',
        text='Préparez-vous à commencer\n\n2',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    PausePrep1 = visual.TextStim(win=win, name='PausePrep1',
        text='Préparez-vous à commencer\n\n1',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "TrainingTrial" ---
    # Run 'Begin Experiment' code from codeCurrImg
    ntrial = 0
    displayDigit = visual.TextStim(win=win, name='displayDigit',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_trainMF = keyboard.Keyboard()
    
    # --- Initialize components for Routine "FeedbackTraining" ---
    textFeedback = visual.TextStim(win=win, name='textFeedback',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "StartExpe" ---
    textStartExp = visual.TextStim(win=win, name='textStartExp',
        text="Bravo! Vous avez terminé l'entraînement.\nVous allez pouvoir commencer la réelle expérience. \n\nGardez en tête : \nÀ chaque fois qu'un chiffre apparaît, appuyez sur la barre d'espace, SAUF pour le chiffre 3 !\n\nAppuyez sur la barre d'espace pour commencer l'experience...\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard()
    pause_beforestart = visual.TextStim(win=win, name='pause_beforestart',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "SetBlock" ---
    
    # --- Initialize components for Routine "Pause" ---
    PausePrep3 = visual.TextStim(win=win, name='PausePrep3',
        text='Préparez-vous à commencer\n\n3',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    PausePrep2 = visual.TextStim(win=win, name='PausePrep2',
        text='Préparez-vous à commencer\n\n2',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    PausePrep1 = visual.TextStim(win=win, name='PausePrep1',
        text='Préparez-vous à commencer\n\n1',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "SetTrial" ---
    
    # --- Initialize components for Routine "TrialBlock" ---
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_testMF = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Mindstate" ---
    # Run 'Begin Experiment' code from codeProbe1
    ans_probe1 = [
    "J'étais concentré-e sur la tâche.",
    "J'étais distrait·e par quelque chose de relatif à la tâche.",
    "J'étais distrait·e par quelque chose dans la pièce.",
    "J'étais distrait·e par quelque chose de personnel, non relatif à la tâche.", 
    "Je ne pensais à rien.",
    "J'ai oublié ce à quoi je pensais."
    ]
    textProbe1 = visual.TextStim(win=win, name='textProbe1',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_respProbe1 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Volition" ---
    textProbe2 = visual.TextStim(win=win, name='textProbe2',
        text='Votre état mental était-il volontaire:\n\n1. Oui\n\n2. Non',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_respProbe2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Fatigue" ---
    textProbe6 = visual.TextStim(win=win, name='textProbe6',
        text="Notez votre vigilance juste avant l'interruption :\n\n1. Très alerte\n\n2. Alerte\n\n3. Un peu alerte\n\n4. Un peu fatigué-e\n\n5. Fatigué-e\n\n6. Très fatigué-e",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_respProbe6 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "PauseBlockTrial" ---
    TxtPauseBlock = visual.TextStim(win=win, name='TxtPauseBlock',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_respPauseBlock = keyboard.Keyboard()
    
    # --- Initialize components for Routine "EndScreen" ---
    TextEnd = visual.TextStim(win=win, name='TextEnd',
        text="Bravo, vous avez terminé le test! \n\nMerci d'avoir participé à cette étude!\n\nVous pouvez appeler l'expérimentateur.",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "SART_Parameters" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('SART_Parameters.started', globalClock.getTime())
    # keep track of which components have finished
    SART_ParametersComponents = []
    for thisComponent in SART_ParametersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SART_Parameters" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SART_ParametersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SART_Parameters" ---
    for thisComponent in SART_ParametersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('SART_Parameters.stopped', globalClock.getTime())
    # the Routine "SART_Parameters" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instru1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instru1.started', globalClock.getTime())
    key_instru_1.keys = []
    key_instru_1.rt = []
    _key_instru_1_allKeys = []
    # keep track of which components have finished
    Instru1Components = [Instru_1, key_instru_1]
    for thisComponent in Instru1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instru1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instru_1* updates
        
        # if Instru_1 is starting this frame...
        if Instru_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Instru_1.frameNStart = frameN  # exact frame index
            Instru_1.tStart = t  # local t and not account for scr refresh
            Instru_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instru_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instru_1.started')
            # update status
            Instru_1.status = STARTED
            Instru_1.setAutoDraw(True)
        
        # if Instru_1 is active this frame...
        if Instru_1.status == STARTED:
            # update params
            pass
        
        # *key_instru_1* updates
        waitOnFlip = False
        
        # if key_instru_1 is starting this frame...
        if key_instru_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_instru_1.frameNStart = frameN  # exact frame index
            key_instru_1.tStart = t  # local t and not account for scr refresh
            key_instru_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instru_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instru_1.started')
            # update status
            key_instru_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instru_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instru_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instru_1.status == STARTED and not waitOnFlip:
            theseKeys = key_instru_1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instru_1_allKeys.extend(theseKeys)
            if len(_key_instru_1_allKeys):
                key_instru_1.keys = _key_instru_1_allKeys[-1].name  # just the last key pressed
                key_instru_1.rt = _key_instru_1_allKeys[-1].rt
                key_instru_1.duration = _key_instru_1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instru1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instru1" ---
    for thisComponent in Instru1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instru1.stopped', globalClock.getTime())
    # check responses
    if key_instru_1.keys in ['', [], None]:  # No response was made
        key_instru_1.keys = None
    thisExp.addData('key_instru_1.keys',key_instru_1.keys)
    if key_instru_1.keys != None:  # we had a response
        thisExp.addData('key_instru_1.rt', key_instru_1.rt)
        thisExp.addData('key_instru_1.duration', key_instru_1.duration)
    thisExp.nextEntry()
    # the Routine "Instru1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instru_Probes" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instru_Probes.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    Instru_ProbesComponents = [InstruProbes, key_resp]
    for thisComponent in Instru_ProbesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instru_Probes" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstruProbes* updates
        
        # if InstruProbes is starting this frame...
        if InstruProbes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstruProbes.frameNStart = frameN  # exact frame index
            InstruProbes.tStart = t  # local t and not account for scr refresh
            InstruProbes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstruProbes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstruProbes.started')
            # update status
            InstruProbes.status = STARTED
            InstruProbes.setAutoDraw(True)
        
        # if InstruProbes is active this frame...
        if InstruProbes.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instru_ProbesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instru_Probes" ---
    for thisComponent in Instru_ProbesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instru_Probes.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Instru_Probes" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instru3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instru3.started', globalClock.getTime())
    key_instru_3.keys = []
    key_instru_3.rt = []
    _key_instru_3_allKeys = []
    # keep track of which components have finished
    Instru3Components = [Instru_3, key_instru_3]
    for thisComponent in Instru3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instru3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instru_3* updates
        
        # if Instru_3 is starting this frame...
        if Instru_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instru_3.frameNStart = frameN  # exact frame index
            Instru_3.tStart = t  # local t and not account for scr refresh
            Instru_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instru_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instru_3.started')
            # update status
            Instru_3.status = STARTED
            Instru_3.setAutoDraw(True)
        
        # if Instru_3 is active this frame...
        if Instru_3.status == STARTED:
            # update params
            pass
        
        # *key_instru_3* updates
        waitOnFlip = False
        
        # if key_instru_3 is starting this frame...
        if key_instru_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instru_3.frameNStart = frameN  # exact frame index
            key_instru_3.tStart = t  # local t and not account for scr refresh
            key_instru_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instru_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instru_3.started')
            # update status
            key_instru_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instru_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instru_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instru_3.status == STARTED and not waitOnFlip:
            theseKeys = key_instru_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instru_3_allKeys.extend(theseKeys)
            if len(_key_instru_3_allKeys):
                key_instru_3.keys = _key_instru_3_allKeys[-1].name  # just the last key pressed
                key_instru_3.rt = _key_instru_3_allKeys[-1].rt
                key_instru_3.duration = _key_instru_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instru3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instru3" ---
    for thisComponent in Instru3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instru3.stopped', globalClock.getTime())
    # check responses
    if key_instru_3.keys in ['', [], None]:  # No response was made
        key_instru_3.keys = None
    thisExp.addData('key_instru_3.keys',key_instru_3.keys)
    if key_instru_3.keys != None:  # we had a response
        thisExp.addData('key_instru_3.rt', key_instru_3.rt)
        thisExp.addData('key_instru_3.duration', key_instru_3.duration)
    thisExp.nextEntry()
    # the Routine "Instru3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Pause.started', globalClock.getTime())
    # keep track of which components have finished
    PauseComponents = [PausePrep3, PausePrep2, PausePrep1]
    for thisComponent in PauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Pause" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PausePrep3* updates
        
        # if PausePrep3 is starting this frame...
        if PausePrep3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PausePrep3.frameNStart = frameN  # exact frame index
            PausePrep3.tStart = t  # local t and not account for scr refresh
            PausePrep3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PausePrep3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PausePrep3.started')
            # update status
            PausePrep3.status = STARTED
            PausePrep3.setAutoDraw(True)
        
        # if PausePrep3 is active this frame...
        if PausePrep3.status == STARTED:
            # update params
            pass
        
        # if PausePrep3 is stopping this frame...
        if PausePrep3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PausePrep3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                PausePrep3.tStop = t  # not accounting for scr refresh
                PausePrep3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PausePrep3.stopped')
                # update status
                PausePrep3.status = FINISHED
                PausePrep3.setAutoDraw(False)
        
        # *PausePrep2* updates
        
        # if PausePrep2 is starting this frame...
        if PausePrep2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            PausePrep2.frameNStart = frameN  # exact frame index
            PausePrep2.tStart = t  # local t and not account for scr refresh
            PausePrep2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PausePrep2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PausePrep2.started')
            # update status
            PausePrep2.status = STARTED
            PausePrep2.setAutoDraw(True)
        
        # if PausePrep2 is active this frame...
        if PausePrep2.status == STARTED:
            # update params
            pass
        
        # if PausePrep2 is stopping this frame...
        if PausePrep2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PausePrep2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                PausePrep2.tStop = t  # not accounting for scr refresh
                PausePrep2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PausePrep2.stopped')
                # update status
                PausePrep2.status = FINISHED
                PausePrep2.setAutoDraw(False)
        
        # *PausePrep1* updates
        
        # if PausePrep1 is starting this frame...
        if PausePrep1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            PausePrep1.frameNStart = frameN  # exact frame index
            PausePrep1.tStart = t  # local t and not account for scr refresh
            PausePrep1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PausePrep1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PausePrep1.started')
            # update status
            PausePrep1.status = STARTED
            PausePrep1.setAutoDraw(True)
        
        # if PausePrep1 is active this frame...
        if PausePrep1.status == STARTED:
            # update params
            pass
        
        # if PausePrep1 is stopping this frame...
        if PausePrep1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PausePrep1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                PausePrep1.tStop = t  # not accounting for scr refresh
                PausePrep1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PausePrep1.stopped')
                # update status
                PausePrep1.status = FINISHED
                PausePrep1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Pause" ---
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Pause.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    LoopTraining = data.TrialHandler(nReps=dur_Training, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='LoopTraining')
    thisExp.addLoop(LoopTraining)  # add the loop to the experiment
    thisLoopTraining = LoopTraining.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopTraining.rgb)
    if thisLoopTraining != None:
        for paramName in thisLoopTraining:
            globals()[paramName] = thisLoopTraining[paramName]
    
    for thisLoopTraining in LoopTraining:
        currentLoop = LoopTraining
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoopTraining.rgb)
        if thisLoopTraining != None:
            for paramName in thisLoopTraining:
                globals()[paramName] = thisLoopTraining[paramName]
        
        # --- Prepare to start Routine "TrainingTrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('TrainingTrial.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeCurrImg
        # pick random digit
        currDigit = training_digits[training_order[ntrial]]
        # pick random duration
        currDuration = training_duration[training_order[ntrial]]
        # is target or not
        if currDigit != 3 :
            currIsTarget = "Go"
        else :
            currIsTarget = "NoGo"
        
        # Save Exp Data
        thisExp.addData('train_digit', currDigit)
        thisExp.addData('train_duration', currDuration)
        thisExp.addData('train_istarget', currIsTarget)
        
        
        displayDigit.setText(currDigit)
        key_resp_trainMF.keys = []
        key_resp_trainMF.rt = []
        _key_resp_trainMF_allKeys = []
        # keep track of which components have finished
        TrainingTrialComponents = [displayDigit, key_resp_trainMF]
        for thisComponent in TrainingTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TrainingTrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *displayDigit* updates
            
            # if displayDigit is starting this frame...
            if displayDigit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                displayDigit.frameNStart = frameN  # exact frame index
                displayDigit.tStart = t  # local t and not account for scr refresh
                displayDigit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(displayDigit, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'displayDigit.started')
                # update status
                displayDigit.status = STARTED
                displayDigit.setAutoDraw(True)
            
            # if displayDigit is active this frame...
            if displayDigit.status == STARTED:
                # update params
                pass
            
            # if displayDigit is stopping this frame...
            if displayDigit.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > displayDigit.tStartRefresh + currDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    displayDigit.tStop = t  # not accounting for scr refresh
                    displayDigit.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'displayDigit.stopped')
                    # update status
                    displayDigit.status = FINISHED
                    displayDigit.setAutoDraw(False)
            
            # *key_resp_trainMF* updates
            waitOnFlip = False
            
            # if key_resp_trainMF is starting this frame...
            if key_resp_trainMF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_trainMF.frameNStart = frameN  # exact frame index
                key_resp_trainMF.tStart = t  # local t and not account for scr refresh
                key_resp_trainMF.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_trainMF, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_trainMF.started')
                # update status
                key_resp_trainMF.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_trainMF.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_trainMF.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_trainMF is stopping this frame...
            if key_resp_trainMF.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_trainMF.tStartRefresh + currDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_trainMF.tStop = t  # not accounting for scr refresh
                    key_resp_trainMF.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_trainMF.stopped')
                    # update status
                    key_resp_trainMF.status = FINISHED
                    key_resp_trainMF.status = FINISHED
            if key_resp_trainMF.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_trainMF.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_trainMF_allKeys.extend(theseKeys)
                if len(_key_resp_trainMF_allKeys):
                    key_resp_trainMF.keys = _key_resp_trainMF_allKeys[-1].name  # just the last key pressed
                    key_resp_trainMF.rt = _key_resp_trainMF_allKeys[-1].rt
                    key_resp_trainMF.duration = _key_resp_trainMF_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_trainMF.keys == str('')) or (key_resp_trainMF.keys == ''):
                        key_resp_trainMF.corr = 1
                    else:
                        key_resp_trainMF.corr = 0
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrainingTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TrainingTrial" ---
        for thisComponent in TrainingTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('TrainingTrial.stopped', globalClock.getTime())
        # Run 'End Routine' code from codeCurrImg
        ntrial += 1
        # check responses
        if key_resp_trainMF.keys in ['', [], None]:  # No response was made
            key_resp_trainMF.keys = None
            # was no response the correct answer?!
            if str('').lower() == 'none':
               key_resp_trainMF.corr = 1;  # correct non-response
            else:
               key_resp_trainMF.corr = 0;  # failed to respond (incorrectly)
        # store data for LoopTraining (TrialHandler)
        LoopTraining.addData('key_resp_trainMF.keys',key_resp_trainMF.keys)
        LoopTraining.addData('key_resp_trainMF.corr', key_resp_trainMF.corr)
        if key_resp_trainMF.keys != None:  # we had a response
            LoopTraining.addData('key_resp_trainMF.rt', key_resp_trainMF.rt)
            LoopTraining.addData('key_resp_trainMF.duration', key_resp_trainMF.duration)
        # the Routine "TrainingTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "FeedbackTraining" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('FeedbackTraining.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeFeedback
        if currIsTarget == 'Go' and key_resp_trainMF.keys == 'space' :
            feedback_text = "Bravo !"
        elif currIsTarget == 'NoGo' and key_resp_trainMF.keys == 'space' :
            feedback_text = "Attention!\n\nIl ne faut pas appuyer quand c'est le chiffre 3"
        elif currIsTarget == 'NoGo' and key_resp_trainMF.keys == None:
            feedback_text = "Bravo de vous être retenu·e!"
        else :
            feedback_text = "N'oubliez pas d'appuyer sur la barre espace!"
        textFeedback.setText(feedback_text)
        # keep track of which components have finished
        FeedbackTrainingComponents = [textFeedback]
        for thisComponent in FeedbackTrainingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "FeedbackTraining" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textFeedback* updates
            
            # if textFeedback is starting this frame...
            if textFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedback.frameNStart = frameN  # exact frame index
                textFeedback.tStart = t  # local t and not account for scr refresh
                textFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textFeedback.started')
                # update status
                textFeedback.status = STARTED
                textFeedback.setAutoDraw(True)
            
            # if textFeedback is active this frame...
            if textFeedback.status == STARTED:
                # update params
                pass
            
            # if textFeedback is stopping this frame...
            if textFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedback.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedback.tStop = t  # not accounting for scr refresh
                    textFeedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textFeedback.stopped')
                    # update status
                    textFeedback.status = FINISHED
                    textFeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackTrainingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FeedbackTraining" ---
        for thisComponent in FeedbackTrainingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('FeedbackTraining.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed dur_Training repeats of 'LoopTraining'
    
    
    # --- Prepare to start Routine "StartExpe" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('StartExpe.started', globalClock.getTime())
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # Run 'Begin Routine' code from set_blockto0
    current_block = 0
    # keep track of which components have finished
    StartExpeComponents = [textStartExp, key_resp_3, pause_beforestart]
    for thisComponent in StartExpeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "StartExpe" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textStartExp* updates
        
        # if textStartExp is starting this frame...
        if textStartExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textStartExp.frameNStart = frameN  # exact frame index
            textStartExp.tStart = t  # local t and not account for scr refresh
            textStartExp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textStartExp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textStartExp.started')
            # update status
            textStartExp.status = STARTED
            textStartExp.setAutoDraw(True)
        
        # if textStartExp is active this frame...
        if textStartExp.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *pause_beforestart* updates
        
        # if pause_beforestart is starting this frame...
        if pause_beforestart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pause_beforestart.frameNStart = frameN  # exact frame index
            pause_beforestart.tStart = t  # local t and not account for scr refresh
            pause_beforestart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pause_beforestart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pause_beforestart.started')
            # update status
            pause_beforestart.status = STARTED
            pause_beforestart.setAutoDraw(True)
        
        # if pause_beforestart is active this frame...
        if pause_beforestart.status == STARTED:
            # update params
            pass
        
        # if pause_beforestart is stopping this frame...
        if pause_beforestart.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pause_beforestart.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pause_beforestart.tStop = t  # not accounting for scr refresh
                pause_beforestart.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pause_beforestart.stopped')
                # update status
                pause_beforestart.status = FINISHED
                pause_beforestart.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StartExpeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "StartExpe" ---
    for thisComponent in StartExpeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('StartExpe.stopped', globalClock.getTime())
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "StartExpe" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LoopBlock = data.TrialHandler(nReps=nBlock, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='LoopBlock')
    thisExp.addLoop(LoopBlock)  # add the loop to the experiment
    thisLoopBlock = LoopBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopBlock.rgb)
    if thisLoopBlock != None:
        for paramName in thisLoopBlock:
            globals()[paramName] = thisLoopBlock[paramName]
    
    for thisLoopBlock in LoopBlock:
        currentLoop = LoopBlock
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoopBlock.rgb)
        if thisLoopBlock != None:
            for paramName in thisLoopBlock:
                globals()[paramName] = thisLoopBlock[paramName]
        
        # --- Prepare to start Routine "SetBlock" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('SetBlock.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeSetBlock
        #Define ≠ len of trials in a list
        listDurTrial = []
        
        for i in range(nTrial - 1) :
            listDurTrial.append(randchoice(durTrial))
        
        listDurTrial.append(randchoice(doubledurTrial))
        
        #Create order variable to shuffle'em
        order_durTrial = []
        # nTrial = len(listDurTrial)
        for i in range(nTrial):
            order_durTrial.append(i)
        shuffle(order_durTrial)
        #follow n_trial
        
        # keep track of which components have finished
        SetBlockComponents = []
        for thisComponent in SetBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SetBlock" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SetBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SetBlock" ---
        for thisComponent in SetBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('SetBlock.stopped', globalClock.getTime())
        # the Routine "SetBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        LoopProbe = data.TrialHandler(nReps=nTrial, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='LoopProbe')
        thisExp.addLoop(LoopProbe)  # add the loop to the experiment
        thisLoopProbe = LoopProbe.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoopProbe.rgb)
        if thisLoopProbe != None:
            for paramName in thisLoopProbe:
                globals()[paramName] = thisLoopProbe[paramName]
        
        for thisLoopProbe in LoopProbe:
            currentLoop = LoopProbe
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoopProbe.rgb)
            if thisLoopProbe != None:
                for paramName in thisLoopProbe:
                    globals()[paramName] = thisLoopProbe[paramName]
            
            # --- Prepare to start Routine "Pause" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Pause.started', globalClock.getTime())
            # keep track of which components have finished
            PauseComponents = [PausePrep3, PausePrep2, PausePrep1]
            for thisComponent in PauseComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Pause" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 3.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PausePrep3* updates
                
                # if PausePrep3 is starting this frame...
                if PausePrep3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PausePrep3.frameNStart = frameN  # exact frame index
                    PausePrep3.tStart = t  # local t and not account for scr refresh
                    PausePrep3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PausePrep3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PausePrep3.started')
                    # update status
                    PausePrep3.status = STARTED
                    PausePrep3.setAutoDraw(True)
                
                # if PausePrep3 is active this frame...
                if PausePrep3.status == STARTED:
                    # update params
                    pass
                
                # if PausePrep3 is stopping this frame...
                if PausePrep3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PausePrep3.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        PausePrep3.tStop = t  # not accounting for scr refresh
                        PausePrep3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PausePrep3.stopped')
                        # update status
                        PausePrep3.status = FINISHED
                        PausePrep3.setAutoDraw(False)
                
                # *PausePrep2* updates
                
                # if PausePrep2 is starting this frame...
                if PausePrep2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    PausePrep2.frameNStart = frameN  # exact frame index
                    PausePrep2.tStart = t  # local t and not account for scr refresh
                    PausePrep2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PausePrep2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PausePrep2.started')
                    # update status
                    PausePrep2.status = STARTED
                    PausePrep2.setAutoDraw(True)
                
                # if PausePrep2 is active this frame...
                if PausePrep2.status == STARTED:
                    # update params
                    pass
                
                # if PausePrep2 is stopping this frame...
                if PausePrep2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PausePrep2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        PausePrep2.tStop = t  # not accounting for scr refresh
                        PausePrep2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PausePrep2.stopped')
                        # update status
                        PausePrep2.status = FINISHED
                        PausePrep2.setAutoDraw(False)
                
                # *PausePrep1* updates
                
                # if PausePrep1 is starting this frame...
                if PausePrep1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    PausePrep1.frameNStart = frameN  # exact frame index
                    PausePrep1.tStart = t  # local t and not account for scr refresh
                    PausePrep1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PausePrep1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PausePrep1.started')
                    # update status
                    PausePrep1.status = STARTED
                    PausePrep1.setAutoDraw(True)
                
                # if PausePrep1 is active this frame...
                if PausePrep1.status == STARTED:
                    # update params
                    pass
                
                # if PausePrep1 is stopping this frame...
                if PausePrep1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PausePrep1.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        PausePrep1.tStop = t  # not accounting for scr refresh
                        PausePrep1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PausePrep1.stopped')
                        # update status
                        PausePrep1.status = FINISHED
                        PausePrep1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PauseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Pause" ---
            for thisComponent in PauseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Pause.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.000000)
            
            # --- Prepare to start Routine "SetTrial" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('SetTrial.started', globalClock.getTime())
            # Run 'Begin Routine' code from codeSetTrial
            trialDurations = []
            current_trial = 0
            
            durCurTrial = listDurTrial[order_durTrial[current_trial]]
            
            while sum(trialDurations) < durCurTrial:
                trialDurations.append(randchoice(durImg))
            nDigits = len(trialDurations)
            
            trial_digits = []
            for i in range(nDigits) :
                if i < perGo * nDigits :
                    trial_digits.append(randchoice(go_digits))
                else :
                    trial_digits.append(nogo_digit)
            trial_order = [i for i in range(nDigits)]
            shuffle(trial_order)
            
            
            # keep track of which components have finished
            SetTrialComponents = []
            for thisComponent in SetTrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "SetTrial" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in SetTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "SetTrial" ---
            for thisComponent in SetTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('SetTrial.stopped', globalClock.getTime())
            # the Routine "SetTrial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            LoopnTrial = data.TrialHandler(nReps=nDigits, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='LoopnTrial')
            thisExp.addLoop(LoopnTrial)  # add the loop to the experiment
            thisLoopnTrial = LoopnTrial.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisLoopnTrial.rgb)
            if thisLoopnTrial != None:
                for paramName in thisLoopnTrial:
                    globals()[paramName] = thisLoopnTrial[paramName]
            
            for thisLoopnTrial in LoopnTrial:
                currentLoop = LoopnTrial
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisLoopnTrial.rgb)
                if thisLoopnTrial != None:
                    for paramName in thisLoopnTrial:
                        globals()[paramName] = thisLoopnTrial[paramName]
                
                # --- Prepare to start Routine "TrialBlock" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('TrialBlock.started', globalClock.getTime())
                # Run 'Begin Routine' code from codeTrial
                #Add needed informations to data_sheet:
                currDigit = trial_digits[trial_order[current_trial]]
                currDuration = trialDurations[trial_order[current_trial]]
                if currDigit != 3 :
                    currIsTarget = 'Go'
                else : 
                    currIsTarget = 'NoGo'
                
                #block, trial & image number 
                thisExp.addData('nBlock', current_block)
                thisExp.addData('nTrial', current_trial)
                thisExp.addData('digit', currDigit)
                #duration of presentation
                thisExp.addData('trial_duration_digit', currDuration)
                #trial_img name, type & istarget
                thisExp.addData('trial_isTarget', currIsTarget)  
                text.setText(currDigit)
                key_resp_testMF.keys = []
                key_resp_testMF.rt = []
                _key_resp_testMF_allKeys = []
                # keep track of which components have finished
                TrialBlockComponents = [text, key_resp_testMF]
                for thisComponent in TrialBlockComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "TrialBlock" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text* updates
                    
                    # if text is starting this frame...
                    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text.frameNStart = frameN  # exact frame index
                        text.tStart = t  # local t and not account for scr refresh
                        text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.started')
                        # update status
                        text.status = STARTED
                        text.setAutoDraw(True)
                    
                    # if text is active this frame...
                    if text.status == STARTED:
                        # update params
                        pass
                    
                    # if text is stopping this frame...
                    if text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text.tStartRefresh + currDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            text.tStop = t  # not accounting for scr refresh
                            text.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text.stopped')
                            # update status
                            text.status = FINISHED
                            text.setAutoDraw(False)
                    
                    # *key_resp_testMF* updates
                    waitOnFlip = False
                    
                    # if key_resp_testMF is starting this frame...
                    if key_resp_testMF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_testMF.frameNStart = frameN  # exact frame index
                        key_resp_testMF.tStart = t  # local t and not account for scr refresh
                        key_resp_testMF.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_testMF, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_testMF.started')
                        # update status
                        key_resp_testMF.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_testMF.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_testMF.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if key_resp_testMF is stopping this frame...
                    if key_resp_testMF.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > key_resp_testMF.tStartRefresh + currDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            key_resp_testMF.tStop = t  # not accounting for scr refresh
                            key_resp_testMF.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'key_resp_testMF.stopped')
                            # update status
                            key_resp_testMF.status = FINISHED
                            key_resp_testMF.status = FINISHED
                    if key_resp_testMF.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_testMF.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_testMF_allKeys.extend(theseKeys)
                        if len(_key_resp_testMF_allKeys):
                            key_resp_testMF.keys = _key_resp_testMF_allKeys[-1].name  # just the last key pressed
                            key_resp_testMF.rt = _key_resp_testMF_allKeys[-1].rt
                            key_resp_testMF.duration = _key_resp_testMF_allKeys[-1].duration
                            # was this correct?
                            if (key_resp_testMF.keys == str('')) or (key_resp_testMF.keys == ''):
                                key_resp_testMF.corr = 1
                            else:
                                key_resp_testMF.corr = 0
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in TrialBlockComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "TrialBlock" ---
                for thisComponent in TrialBlockComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('TrialBlock.stopped', globalClock.getTime())
                # Run 'End Routine' code from codeTrial
                current_trial += 1
                # check responses
                if key_resp_testMF.keys in ['', [], None]:  # No response was made
                    key_resp_testMF.keys = None
                    # was no response the correct answer?!
                    if str('').lower() == 'none':
                       key_resp_testMF.corr = 1;  # correct non-response
                    else:
                       key_resp_testMF.corr = 0;  # failed to respond (incorrectly)
                # store data for LoopnTrial (TrialHandler)
                LoopnTrial.addData('key_resp_testMF.keys',key_resp_testMF.keys)
                LoopnTrial.addData('key_resp_testMF.corr', key_resp_testMF.corr)
                if key_resp_testMF.keys != None:  # we had a response
                    LoopnTrial.addData('key_resp_testMF.rt', key_resp_testMF.rt)
                    LoopnTrial.addData('key_resp_testMF.duration', key_resp_testMF.duration)
                # the Routine "TrialBlock" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed nDigits repeats of 'LoopnTrial'
            
            
            # --- Prepare to start Routine "Mindstate" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Mindstate.started', globalClock.getTime())
            # Run 'Begin Routine' code from codeProbe1
            shuffle(ans_probe1)
             
            curransP1_0 = ans_probe1[0]
            curransP1_1 = ans_probe1[1]
            curransP1_2 = ans_probe1[2]
            curransP1_3 = ans_probe1[3]
            curransP1_4 = ans_probe1[4]
            curransP1_5 = ans_probe1[5]
            
            thisExp.addData('curr_ans0_P1', curransP1_0)
            thisExp.addData('curr_ans1_P1', curransP1_1)
            thisExp.addData('curr_ans2_P1', curransP1_2)
            thisExp.addData('curr_ans3_P1', curransP1_3)
            thisExp.addData('curr_ans4_p1', curransP1_4)
            thisExp.addData('curr_ans5_p1', curransP1_5)
            
            thisExp.addData('Probe1',"Mindstate")
            
            textProbe1.setText("Choississez la réponse qui convient le mieux à votre état dans les quelques secondes avant l'interruption\nDans quel état étiez vous :" + "\n\n 1. " + curransP1_0 +"\n\n 2. " + curransP1_1 + "\n\n 3. " + curransP1_2 + "\n\n 4. " + curransP1_3 + "\n\n 5. " + curransP1_4  + "\n\n 6. " + curransP1_5)
            key_respProbe1.keys = []
            key_respProbe1.rt = []
            _key_respProbe1_allKeys = []
            # keep track of which components have finished
            MindstateComponents = [textProbe1, key_respProbe1]
            for thisComponent in MindstateComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Mindstate" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textProbe1* updates
                
                # if textProbe1 is starting this frame...
                if textProbe1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textProbe1.frameNStart = frameN  # exact frame index
                    textProbe1.tStart = t  # local t and not account for scr refresh
                    textProbe1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textProbe1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textProbe1.started')
                    # update status
                    textProbe1.status = STARTED
                    textProbe1.setAutoDraw(True)
                
                # if textProbe1 is active this frame...
                if textProbe1.status == STARTED:
                    # update params
                    pass
                
                # *key_respProbe1* updates
                waitOnFlip = False
                
                # if key_respProbe1 is starting this frame...
                if key_respProbe1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_respProbe1.frameNStart = frameN  # exact frame index
                    key_respProbe1.tStart = t  # local t and not account for scr refresh
                    key_respProbe1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_respProbe1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_respProbe1.started')
                    # update status
                    key_respProbe1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_respProbe1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_respProbe1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_respProbe1.status == STARTED and not waitOnFlip:
                    theseKeys = key_respProbe1.getKeys(keyList=['1', '2', '3', '4', '5', '6'], ignoreKeys=["escape"], waitRelease=False)
                    _key_respProbe1_allKeys.extend(theseKeys)
                    if len(_key_respProbe1_allKeys):
                        key_respProbe1.keys = _key_respProbe1_allKeys[-1].name  # just the last key pressed
                        key_respProbe1.rt = _key_respProbe1_allKeys[-1].rt
                        key_respProbe1.duration = _key_respProbe1_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MindstateComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Mindstate" ---
            for thisComponent in MindstateComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Mindstate.stopped', globalClock.getTime())
            # check responses
            if key_respProbe1.keys in ['', [], None]:  # No response was made
                key_respProbe1.keys = None
            LoopProbe.addData('key_respProbe1.keys',key_respProbe1.keys)
            if key_respProbe1.keys != None:  # we had a response
                LoopProbe.addData('key_respProbe1.rt', key_respProbe1.rt)
                LoopProbe.addData('key_respProbe1.duration', key_respProbe1.duration)
            # the Routine "Mindstate" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Volition" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Volition.started', globalClock.getTime())
            # Run 'Begin Routine' code from codeProbe2
            thisExp.addData('Probe2',"Volition")
            
            key_respProbe2.keys = []
            key_respProbe2.rt = []
            _key_respProbe2_allKeys = []
            # keep track of which components have finished
            VolitionComponents = [textProbe2, key_respProbe2]
            for thisComponent in VolitionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Volition" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textProbe2* updates
                
                # if textProbe2 is starting this frame...
                if textProbe2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textProbe2.frameNStart = frameN  # exact frame index
                    textProbe2.tStart = t  # local t and not account for scr refresh
                    textProbe2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textProbe2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textProbe2.started')
                    # update status
                    textProbe2.status = STARTED
                    textProbe2.setAutoDraw(True)
                
                # if textProbe2 is active this frame...
                if textProbe2.status == STARTED:
                    # update params
                    pass
                
                # *key_respProbe2* updates
                waitOnFlip = False
                
                # if key_respProbe2 is starting this frame...
                if key_respProbe2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_respProbe2.frameNStart = frameN  # exact frame index
                    key_respProbe2.tStart = t  # local t and not account for scr refresh
                    key_respProbe2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_respProbe2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_respProbe2.started')
                    # update status
                    key_respProbe2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_respProbe2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_respProbe2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_respProbe2.status == STARTED and not waitOnFlip:
                    theseKeys = key_respProbe2.getKeys(keyList=['1', '2'], ignoreKeys=["escape"], waitRelease=False)
                    _key_respProbe2_allKeys.extend(theseKeys)
                    if len(_key_respProbe2_allKeys):
                        key_respProbe2.keys = _key_respProbe2_allKeys[-1].name  # just the last key pressed
                        key_respProbe2.rt = _key_respProbe2_allKeys[-1].rt
                        key_respProbe2.duration = _key_respProbe2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in VolitionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Volition" ---
            for thisComponent in VolitionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Volition.stopped', globalClock.getTime())
            # check responses
            if key_respProbe2.keys in ['', [], None]:  # No response was made
                key_respProbe2.keys = None
            LoopProbe.addData('key_respProbe2.keys',key_respProbe2.keys)
            if key_respProbe2.keys != None:  # we had a response
                LoopProbe.addData('key_respProbe2.rt', key_respProbe2.rt)
                LoopProbe.addData('key_respProbe2.duration', key_respProbe2.duration)
            # the Routine "Volition" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Fatigue" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Fatigue.started', globalClock.getTime())
            # Run 'Begin Routine' code from codeProbe6
            thisExp.addData('Probe6',"Fatigue")
            key_respProbe6.keys = []
            key_respProbe6.rt = []
            _key_respProbe6_allKeys = []
            # keep track of which components have finished
            FatigueComponents = [textProbe6, key_respProbe6]
            for thisComponent in FatigueComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Fatigue" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textProbe6* updates
                
                # if textProbe6 is starting this frame...
                if textProbe6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textProbe6.frameNStart = frameN  # exact frame index
                    textProbe6.tStart = t  # local t and not account for scr refresh
                    textProbe6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textProbe6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textProbe6.started')
                    # update status
                    textProbe6.status = STARTED
                    textProbe6.setAutoDraw(True)
                
                # if textProbe6 is active this frame...
                if textProbe6.status == STARTED:
                    # update params
                    pass
                
                # *key_respProbe6* updates
                waitOnFlip = False
                
                # if key_respProbe6 is starting this frame...
                if key_respProbe6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_respProbe6.frameNStart = frameN  # exact frame index
                    key_respProbe6.tStart = t  # local t and not account for scr refresh
                    key_respProbe6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_respProbe6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_respProbe6.started')
                    # update status
                    key_respProbe6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_respProbe6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_respProbe6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_respProbe6.status == STARTED and not waitOnFlip:
                    theseKeys = key_respProbe6.getKeys(keyList=['1','2','3','4','5','6'], ignoreKeys=["escape"], waitRelease=False)
                    _key_respProbe6_allKeys.extend(theseKeys)
                    if len(_key_respProbe6_allKeys):
                        key_respProbe6.keys = _key_respProbe6_allKeys[-1].name  # just the last key pressed
                        key_respProbe6.rt = _key_respProbe6_allKeys[-1].rt
                        key_respProbe6.duration = _key_respProbe6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FatigueComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Fatigue" ---
            for thisComponent in FatigueComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Fatigue.stopped', globalClock.getTime())
            # check responses
            if key_respProbe6.keys in ['', [], None]:  # No response was made
                key_respProbe6.keys = None
            LoopProbe.addData('key_respProbe6.keys',key_respProbe6.keys)
            if key_respProbe6.keys != None:  # we had a response
                LoopProbe.addData('key_respProbe6.rt', key_respProbe6.rt)
                LoopProbe.addData('key_respProbe6.duration', key_respProbe6.duration)
            # the Routine "Fatigue" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed nTrial repeats of 'LoopProbe'
        
        
        # --- Prepare to start Routine "PauseBlockTrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('PauseBlockTrial.started', globalClock.getTime())
        # Run 'Begin Routine' code from codePauseBlock
        if current_block == 0 :
            txt_PauseBlock = "Bravo! Vous avez terminé le bloc n°1 !\n\nVous pouvez vous reposer un instant si vous le souhaitez.\n\n< Appuyez sur la barre d'espace pour passer au bloc suivant... >"
        elif current_block == 1 :
            txt_PauseBlock = "Bravo! Vous avez terminé le bloc n°2 !\n\nVous avez fait la moitié, reposez-vous un instant si vous le souhaitez.\n\n< Appuyez sur la barre d'espace pour passer au bloc suivant... >"
        elif current_block == 2 :
            txt_PauseBlock = "Bravo! Vous avez terminé le bloc n°3 !\n\nVous y êtes presques, reposez-vous un instant si vous le souhaitez.\n\n< Appuyez sur la barre d'espace pour passer au bloc suivant... >"
        elif current_block == 3 :
            txt_PauseBlock = "Bravo! Vous avez terminé le bloc n°4 !\n\nVous avez terminé tous les blocs!\n\n< Appuyez sur la barre d'espace pour passer à la suite... >"
        
        TxtPauseBlock.setText(txt_PauseBlock)
        key_respPauseBlock.keys = []
        key_respPauseBlock.rt = []
        _key_respPauseBlock_allKeys = []
        # keep track of which components have finished
        PauseBlockTrialComponents = [TxtPauseBlock, key_respPauseBlock]
        for thisComponent in PauseBlockTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PauseBlockTrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TxtPauseBlock* updates
            
            # if TxtPauseBlock is starting this frame...
            if TxtPauseBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TxtPauseBlock.frameNStart = frameN  # exact frame index
                TxtPauseBlock.tStart = t  # local t and not account for scr refresh
                TxtPauseBlock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TxtPauseBlock, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TxtPauseBlock.started')
                # update status
                TxtPauseBlock.status = STARTED
                TxtPauseBlock.setAutoDraw(True)
            
            # if TxtPauseBlock is active this frame...
            if TxtPauseBlock.status == STARTED:
                # update params
                pass
            
            # *key_respPauseBlock* updates
            waitOnFlip = False
            
            # if key_respPauseBlock is starting this frame...
            if key_respPauseBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respPauseBlock.frameNStart = frameN  # exact frame index
                key_respPauseBlock.tStart = t  # local t and not account for scr refresh
                key_respPauseBlock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respPauseBlock, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_respPauseBlock.started')
                # update status
                key_respPauseBlock.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respPauseBlock.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respPauseBlock.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respPauseBlock.status == STARTED and not waitOnFlip:
                theseKeys = key_respPauseBlock.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_respPauseBlock_allKeys.extend(theseKeys)
                if len(_key_respPauseBlock_allKeys):
                    key_respPauseBlock.keys = _key_respPauseBlock_allKeys[-1].name  # just the last key pressed
                    key_respPauseBlock.rt = _key_respPauseBlock_allKeys[-1].rt
                    key_respPauseBlock.duration = _key_respPauseBlock_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PauseBlockTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PauseBlockTrial" ---
        for thisComponent in PauseBlockTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('PauseBlockTrial.stopped', globalClock.getTime())
        # Run 'End Routine' code from codePauseBlock
        current_block += 1
        # check responses
        if key_respPauseBlock.keys in ['', [], None]:  # No response was made
            key_respPauseBlock.keys = None
        LoopBlock.addData('key_respPauseBlock.keys',key_respPauseBlock.keys)
        if key_respPauseBlock.keys != None:  # we had a response
            LoopBlock.addData('key_respPauseBlock.rt', key_respPauseBlock.rt)
            LoopBlock.addData('key_respPauseBlock.duration', key_respPauseBlock.duration)
        # the Routine "PauseBlockTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed nBlock repeats of 'LoopBlock'
    
    
    # --- Prepare to start Routine "EndScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('EndScreen.started', globalClock.getTime())
    # keep track of which components have finished
    EndScreenComponents = [TextEnd]
    for thisComponent in EndScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TextEnd* updates
        
        # if TextEnd is starting this frame...
        if TextEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TextEnd.frameNStart = frameN  # exact frame index
            TextEnd.tStart = t  # local t and not account for scr refresh
            TextEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TextEnd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TextEnd.started')
            # update status
            TextEnd.status = STARTED
            TextEnd.setAutoDraw(True)
        
        # if TextEnd is active this frame...
        if TextEnd.status == STARTED:
            # update params
            pass
        
        # if TextEnd is stopping this frame...
        if TextEnd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TextEnd.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                TextEnd.tStop = t  # not accounting for scr refresh
                TextEnd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TextEnd.stopped')
                # update status
                TextEnd.status = FINISHED
                TextEnd.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndScreen" ---
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('EndScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
