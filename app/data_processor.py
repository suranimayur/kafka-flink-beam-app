from datetime import datetime
from typing import Dict, Any
from app.logger import setup_logger

logger = setup_logger(__name__)

def calculate_age(date_of_birth: str) -> int:
    """
    Calculate age from date of birth.
    
    Args:
        date_of_birth: Date of birth in YYYY-MM-DD format
        
    Returns:
        Age in years
    """
    try:
        birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except Exception as e:
        logger.error(f"Error calculating age: {str(e)}")
        raise

def process_message(message: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process the incoming message to calculate age and determine if it's even or odd.
    
    Args:
        message: Dictionary containing the message data
        
    Returns:
        Dictionary with processed data including age and even/odd classification
    """
    try:
        # Extract date of birth
        date_of_birth = message.get('date_of_birth')
        if not date_of_birth:
            raise ValueError("date_of_birth is required")
        
        # Calculate age
        age = calculate_age(date_of_birth)
        
        # Prepare processed data
        processed_data = {
            'age': age,
            'is_even': age % 2 == 0,
            'processing_timestamp': datetime.now().isoformat()
        }
        
        return processed_data
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise 