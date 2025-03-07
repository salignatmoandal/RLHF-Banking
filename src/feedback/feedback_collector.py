"""
Module for collecting and managing user feedback.
"""
import sqlite3
import os
from datetime import datetime
from typing import List

class FeedbackCollector:
    def __init__(self):
        self.db_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'data',
            'banking_data.db'
        )
    
    def save_feedback(
        self,
        customer_id: int,
        question: str,
        response: str,
        rating: int,
        selected_policies: List[str]
    ) -> bool:
        """Save feedback to the database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Ensure feedback table exists
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                question TEXT,
                response TEXT,
                rating INTEGER CHECK(rating >= 1 AND rating <= 5),
                selected_policies TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )
            ''')
            
            cursor.execute('''
                INSERT INTO feedback (
                    customer_id, question, response, rating, 
                    selected_policies, timestamp
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                customer_id,
                question,
                response,
                rating,
                ','.join(selected_policies),
                datetime.now()
            ))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Error saving feedback: {e}")
            return False
    
    def get_customer_feedback_history(self, customer_id: int) -> list:
        """Retrieve feedback history for a customer."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT question, response, rating, timestamp 
            FROM feedback 
            WHERE customer_id = ?
            ORDER BY timestamp DESC
        ''', (customer_id,))
        
        results = cursor.fetchall()
        conn.close()
        
        return results 