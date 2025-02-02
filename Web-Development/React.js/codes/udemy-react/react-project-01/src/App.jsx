import Header from './components/Header/Header';
import CoreConcept from './components/CoreConcept/CoreConcept'
import TabButton from './components/TabButton/TabButton';
import { CORE_CONCEPTS, EXAMPLES } from './data'
import { useState } from 'react';

function App() {
  let [selectedTopic, setSelectedTopic] = useState(null);

  function handleSelect(selectedButton) {
    setSelectedTopic(selectedButton);
  }

  return (
    <div>
      <Header />
      <main>
        <section id="core-concepts">
          <h2>Core Concepts</h2>
          <ul>
            {CORE_CONCEPTS.map((concept) => {return <CoreConcept key={concept.title} {...concept}/>})}
          </ul>
        </section>
        <section id="examples">
          <h2>Examples</h2>
          <menu>
            <TabButton isSelected={selectedTopic === 'components'} onSelect={()=>{handleSelect('components')}}>Components</TabButton>
            <TabButton isSelected={selectedTopic === 'jsx'} onSelect={()=>{handleSelect('jsx')}}>JSX</TabButton>
            <TabButton isSelected={selectedTopic === 'props'} onSelect={()=>{handleSelect('props')}}>Props</TabButton>
            <TabButton isSelected={selectedTopic === 'state'} onSelect={()=>{handleSelect('state')}}>State</TabButton>
          </menu>
          {!selectedTopic ? <p>Please click a button</p> : 
            <div id="tab-content">
              <h3>{EXAMPLES[selectedTopic].title}</h3>
              <p>{EXAMPLES[selectedTopic].description}</p>
              <pre>
                <code>
                  {EXAMPLES[selectedTopic].code}
                </code>
              </pre>
            </div>
          }
        </section>
        <h2>Time to get started!</h2>
      </main>
    </div>
  );
}

export default App;
